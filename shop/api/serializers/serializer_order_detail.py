from rest_framework import serializers

from accounts.api.serializers import BaseAddressSerializer
from shop.api.serializers.base_sending_method import BaseSendingMethodSerializer
from shop.api.serializers.base_order_item import BaseOrderItemSerializer
from shop.models import Order, OrderItem
from accounts.api.serializers.serializer_base_user import BaseUserSerializer


class OrderDetailSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer(read_only=True)
    order_item = serializers.SerializerMethodField()
    sending_method = BaseSendingMethodSerializer()
    address = BaseAddressSerializer()

    class Meta:
        model = Order
        depth = 1
        fields = (
            'id', 'user', 'description', 'status', 'sending_method', 'address',
            'consistency_code', 'email_sent', 'sms_sent', 'get_complete_date',
            'get_created_at', 'get_updated_at',
            'get_created_at_jalali', 'get_updated_at_jalali', 'order_item'
        )

        read_only_fields = (
            'id', 'user', 'description', 'status', 'sending_method',
            'consistency_code', 'email_sent', 'sms_sent', 'get_complete_date',
            'get_created_at', 'get_updated_at',
            'get_created_at_jalali', 'get_updated_at_jalali', 'order_item'
        )

    def get_order_item(self, obj):
        query = OrderItem.objects.filter(
            orders__id=obj.id).select_related("products").order_by('-id')
        return BaseOrderItemSerializer(query, many=True).data
