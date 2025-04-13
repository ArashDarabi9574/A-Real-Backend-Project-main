from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.api.serializers.serializer_base_address import BaseAddressUpdateSerializer


class UserInfoForInvoiceSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name')
    address = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ("phone_number", "national_number", "full_name", "address")

    def get_address(self, obj):
        if obj.address is not None:
            result = obj.address.get_full_address
        else:
            result = 'not set'

        return result
