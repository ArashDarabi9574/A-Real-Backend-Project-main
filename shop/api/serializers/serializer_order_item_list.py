from rest_framework import serializers

from shop.api.serializers import BaseProductSerializer
from shop.api.serializers.base_order import BaseOrderSerializer
from shop.api.serializers.base_branch import BaseBranchSerializer
from shop.models import OrderItem


class OrderItemListSerializer(serializers.ModelSerializer):
    products = BaseProductSerializer(read_only=True)
    orders = BaseOrderSerializer(read_only=True)
    branches = BaseBranchSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = (
            'id', 'orders', 'products', 'main_price', 'quantity',
            'branches'
        )

        read_only_fields = (
            'id', 'orders', 'products', 'main_price', 'quantity',
            'branches'
        )
