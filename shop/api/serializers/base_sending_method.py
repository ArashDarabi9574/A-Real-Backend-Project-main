from rest_framework import serializers
from shop.models import SendingMethod


class BaseSendingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendingMethod
        fields = ('id', 'title', 'price', 'free_price')
