from rest_framework import serializers
from shop.models import SendingMethod


class SendingMethodCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendingMethod
        fields = ('title', 'price', 'free_price',
                  'status', 'description', 'state')
