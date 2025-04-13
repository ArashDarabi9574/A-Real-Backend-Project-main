from rest_framework import serializers

from shop.models import OrderItem
from shop.api.serializers.base_products import BaseProductSerializer


class BaseOrderItemSerializer(serializers.ModelSerializer):
    products = BaseProductSerializer()

    class Meta:
        model = OrderItem
        fields = ('id', 'products', 'quantity', 'main_price', 'paid_price')
        read_only_fields = ('id', 'products', 'quantity',
                            'main_price', 'paid_price')
