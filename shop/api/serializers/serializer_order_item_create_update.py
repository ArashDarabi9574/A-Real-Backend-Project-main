from rest_framework import serializers
from shop.models import OrderItem


class OrderItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('products', 'orders', 'quantity')
