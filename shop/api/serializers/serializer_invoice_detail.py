from rest_framework import serializers
from shop.models import Invoice


class InvoiceDetailSerializer(serializers.ModelSerializer):
    date = serializers.CharField(source='get_created_at_jalali')

    class Meta:
        model = Invoice
        fields = ('invoice_number', 'date')
