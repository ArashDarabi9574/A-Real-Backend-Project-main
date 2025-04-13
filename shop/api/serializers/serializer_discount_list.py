from rest_framework import serializers

from shop.models import Discount


class DiscountListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = ('id', 'code', 'title', 'type_discount', 'type_action', 'percentage',
                  'amount_discount', 'get_expired_date', 'get_expired_date_jalali',
                  'get_created_at', 'get_created_at_jalali',)

        read_only_fields = ('id', 'code', 'title', 'type_discount', 'type_action', 'percentage',
                            'amount_discount', 'get_expired_date', 'get_expired_date_jalali',
                            'get_created_at', 'get_created_at_jalali',)
