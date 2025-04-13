from rest_framework import serializers

from shop.models import Discount


class DiscountCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = ('title', 'code', 'type_discount', 'type_action', 'percentage',
                  'amount_discount', 'expired_date', 'expired_date_jalali',)

    def validate(self, data):
        if not 0 < int(data['percentage']) <= 100:
            raise serializers.ValidationError(
                "درصد تخفیف باید بین 1 تا 100 باشد!")
        return data
