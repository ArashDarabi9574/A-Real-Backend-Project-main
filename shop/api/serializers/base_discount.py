from rest_framework import serializers

from shop.models import Discount


class BaseDiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = ('id', 'title', 'code', 'percentage',
                  'amount_discount', 'type_action', 'get_expired_date', 'get_expired_date_jalali',)
        read_only_fields = ('id', 'title', 'code', 'percentage',
                            'amount_discount', 'type_action', 'get_expired_date', 'get_expired_date_jalali',)
