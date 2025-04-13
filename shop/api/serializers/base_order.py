from rest_framework import serializers

from shop.models import Order


class BaseOrderSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'user', 'status',
                  'consistency_code', 'get_complete_date')
        read_only_fields = ('id', 'user', 'status',
                            'consistency_code', 'get_complete_date')

    def get_user(self, obj):
        return obj.user.phone_number
