import logging

from django.utils import timezone
from rest_framework import views, permissions

from accounts.models import UserAddress
from shop.models import Order, OrderItem, Discount, SendingMethod, Product, ProductBranch
from payment.views import send_request
from utils.apply_discount_order import apply_discount
from utils.response import unsuccessful_response, successful_response
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Payments"])
class RequestPayment(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'delete', 'patch']

    def post(self, request, *args, **kwargs):
        user = request.user
        products = request.data.get('products', None)
        sending_method_id = request.data.get('sending_method_id', None)
        address_id = request.data.get('address_id', None)
        discount_code = request.data.get('discount_code', None)
        description = request.data.get('description', None)

        if products is None:
            return unsuccessful_response(message='فیلد محصول نمی‌تواند خالی باشد', data={})

        if sending_method_id is None:
            return unsuccessful_response(message='فیلد  ایدی روش ارسال نمی‌تواند خالی باشد', data={})

        # if address_id is None:
        #     return unsuccessful_response(message='فیلد  ایدی ادرس نمی‌تواند خالی باشد', data={})

        if not isinstance(products, list):
            return unsuccessful_response(message='فیلد محصول لازم است یک لیست باشد', data={})

        if address_id is not None:
            address_user = UserAddress.objects.filter(
                id=address_id, user=user).last()
            if address_user is None:
                return unsuccessful_response(message='ادرس یافت نشد', data={})
        else:
            address_user = None

        sending_method = SendingMethod.objects.filter(
            id=sending_method_id).last()
        if sending_method is None:
            return unsuccessful_response(message='روش ارسال یافت نشد', data={})

        order = Order.objects.create(
            user=user, sending_method=sending_method, address=address_user, description=description)

        for item in products:
            product = Product.objects.get(id=item['product_id'])
            branches = product.product_branch.all()
            my_branch = None
            if branches:
                for branch in branches:
                    if branch.inventory is not None and branch.inventory > 0:
                        my_branch = branch.branches
                        # branch.inventory -= 1
                        # branch.save()
                        break
            if my_branch is not None:
                OrderItem.objects.create(
                    orders=order,
                    products=product,
                    quantity=item['quantity'],
                    branches=my_branch,
                )

        if discount_code is not None and discount_code != '':
            discount = Discount.objects.filter(
                code=discount_code,
                expired_date__gte=timezone.now()).last()
            if discount is None:
                return unsuccessful_response(message='کد تخففیف درست نیست', data={"discount_code": discount_code})

            apply_discount(discount_code=discount, order=order)

        return successful_response(
            data={'url': send_request(
                host=request.META['HTTP_HOST'], order_id=order.id)}
        )
