from rest_framework import serializers

from shop.api.serializers.base_sending_method import BaseSendingMethodSerializer
from shop.models import Order, SendingMethod


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'status', 'sending_method', 'description', 'address', 'consistency_code', 'payment_method'
        )


    # def update(self, instance, validated_data):
    #     sending_method_data = validated_data.pop('sending_method', None)
    #     address = validated_data.pop('address', None)
    #     payment_method = validated_data.pop('payment_method', None)
    #     if sending_method_data is not None and sending_method_data.get('title') is not None:
    #         sending_method = SendingMethod.objects.get(title=sending_method_data.get('title'))
    #         instance.sending_method = sending_method
    #         instance.save()

    #     # Now update the order instance with remaining validated data
    #     return super().update(instance, validated_data)
