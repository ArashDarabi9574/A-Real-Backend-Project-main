from rest_framework import serializers
from shop.models import SendingMethod


class SendingMethodForInvoiceSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = SendingMethod
        fields = ('title', 'price', 'description')

    def get_price(self, obj):
        if self.context.get('final_price_of_discounted_products') > obj.free_price and obj.free_price != 0:
            return 0
        return obj.price
