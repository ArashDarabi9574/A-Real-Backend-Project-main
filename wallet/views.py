import json
import requests
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect

from shop.models import Order
from payment.models import Payment
from utils.sender import sms_sender

ZP_MERCHANT = settings.ZP_MERCHANT
ZP_DESCRIPTION = settings.ZP_DESCRIPTION

ZP_API_REQUEST = settings.ZP_API_REQUEST
ZP_API_VERIFY = settings.ZP_API_VERIFY
ZP_API_STARTPAY = settings.ZP_API_STARTPAY


def send_request(host, order_id):
    CALL_BACKE_URL = f'https://' + host + f'/verify/zarrinpal/{order_id}/'
    order = get_object_or_404(Order, pk=order_id)

    data = {
        "merchant_id": ZP_MERCHANT,
        "amount": order.get_total_price,
        "callback_url": CALL_BACKE_URL,
        "description": ZP_DESCRIPTION,
    }
    header = {
        "accept": "application/json",
        "content-type": "application/json'"
    }

    response = requests.post(
        url=ZP_API_REQUEST, data=json.dumps(data), headers=header)

    if len(response.json()['errors']) == 0:
        authority = response.json()['data']['authority']
        return ZP_API_STARTPAY.format(authority=authority)
    else:
        e_code = response.json()['errors']['code']
        e_message = response.json()['errors']['message']
        e_validations = response.json()['errors']['validations']
        return f"Error code: {e_code}, Error Message: {e_message} , validations :{e_validations}"


def verify(request, order_id):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    order = get_object_or_404(Order, pk=order_id)
    amount = order.get_total_price

    new_payment = Payment(order=order, amount=amount, user=order.user)

    if request.GET.get('Status') == 'OK':
        header = {
            "accept": "application/json",
            "content-type": "application/json'"
        }
        data = {
            "merchant_id": ZP_MERCHANT,
            "amount": amount,
            "authority": t_authority
        }

        response = requests.post(
            url=ZP_API_VERIFY, data=json.dumps(data), headers=header)

        if len(response.json()['errors']) == 0:
            t_status = response.json()['data']['code']
            ref_id = response.json()['data']['ref_id']
            if t_status == 100:
                order.status = 2
                order.save()

                new_payment.status = 1
                new_payment.status_code = t_status
                new_payment.ref_code = ref_id
                new_payment.save()

                # send sms
                sms_sender(number=order.user.phone_number, usage='verify_wallet', price=amount)

                return redirect(f'/payment/?order_id={order_id}')

            elif t_status == 101:
                new_payment.status = 0
                new_payment.status_code = t_status
                new_payment.payment_message = response.json()[
                    'data']['message']
                new_payment.save()

                return redirect(f'/payment/?order_id={order_id}')
            else:
                new_payment.status = 0
                new_payment.status_code = t_status
                new_payment.payment_message = str(
                    response.json()['data']['message'])
                new_payment.save()

                return redirect(f'/payment/?order_id={order_id}')
        else:
            e_code = response.json()['errors']['code']
            e_message = response.json()['errors']['message']

            new_payment.status = 0
            new_payment.status_code = e_code
            new_payment.payment_message = e_message
            new_payment.save()

            return redirect(f'/payment/?order_id={order_id}')
    else:
        new_payment.status = 0
        new_payment.status_code = 999
        new_payment.payment_message = 'Transaction failed or canceled by user'
        new_payment.save()

        return redirect(f'/payment/?order_id={order_id}')
