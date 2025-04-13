from rest_framework import serializers
from accounts.models import UserAddress


class BaseAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('postal_code', 'get_full_address')
        add_fieldsets = ('postal_code', 'get_full_address')


class BaseAddressUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('postal_code', 'province', 'city', 'address', 'plaque',
                  'telephone_number', 'reciever')
        add_fieldsets = ('postal_code', 'province',
                         'city', 'address', 'plaque', 'telephone_number', 'reciever')
