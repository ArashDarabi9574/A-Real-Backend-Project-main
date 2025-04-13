from rest_framework import serializers
from shop.models import Invoice
from shop.api.serializers.base_order import BaseOrderSerializer


class InvoiceListSerializer(serializers.ModelSerializer):
    order = BaseOrderSerializer()
    date = serializers.CharField(source='get_created_at_jalali')

    class Meta:
        model = Invoice
        fields = ('order', "invoice_number", 'date')
