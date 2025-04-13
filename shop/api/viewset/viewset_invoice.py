from pprint import pprint

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import views, permissions
from collections import ChainMap

from page.api.serializer import BaseInfoSerializer
from shop.api.serializers import OrderItemForInvoiceSerializer, SendingMethodForInvoiceSerializer, \
    InvoiceDetailSerializer, InvoiceListSerializer
from shop.models import Invoice, Order
from utils.response import unsuccessful_response, successful_response
from accounts.api.serializers import UserInfoForInvoiceSerializer
from page.models import BaseInfo


@extend_schema(tags=["Invoice"])
class InvoiceView(views.APIView):
    model = Invoice

    # permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        consistency_code = request.data.get('id', False)

        if not consistency_code:
            return unsuccessful_response(data={}, message='ارسال "id" ضروری است.')

        # create invoice
        order = get_object_or_404(Order, pk=consistency_code)
        invoice, _ = Invoice.objects.get_or_create(order=order)

        # Buyer information
        serialize_data_buyer_information = {"buyer": UserInfoForInvoiceSerializer(invoice.order.user).data}

        # Product information
        serialize_data_product_information = {
            "product": OrderItemForInvoiceSerializer(invoice.order.order_items.all(), many=True).data}

        final_price_of_discounted_products, total_price_without_discount, total_discount_amount = 0, 0, 0
        for data in serialize_data_product_information['product']:
            total_price_without_discount += int(data['main_price']) * int(data['quantity'])
            if data.get('discount_amount') is not None:
                total_discount_amount += int(data['discount_amount']) * int(data['quantity'])
            final_price_of_discounted_products += int(data['total_price'])

        # Sending information
        serialize_data_sending_information = {
            "sending": SendingMethodForInvoiceSerializer(
                invoice.order.sending_method,
                context={'final_price_of_discounted_products': final_price_of_discounted_products, }).data
        }

        # Invoice information
        serialize_data_invoice_information = {
            "invoice": InvoiceDetailSerializer(invoice).data
        }

        # Base site information
        serialize_data_base_information = {
            "base_info_site": BaseInfoSerializer(BaseInfo.objects.last()).data
        }

        data = ChainMap(
            serialize_data_buyer_information,
            serialize_data_product_information,
            serialize_data_sending_information,
            serialize_data_invoice_information,
            serialize_data_base_information,
        )

        data['total_price_without_discount'] = total_price_without_discount
        data['total_discount_amount'] = total_discount_amount
        data['final_price_of_discounted_products'] = final_price_of_discounted_products

        return successful_response(data=data)

    def get(self, request):
        invoices = self.model.objects.all()
        return successful_response(message='ok', data=InvoiceListSerializer(invoices, many=True).data)
