from rest_framework import serializers
from accounts.models import UserAddress


class AddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('id', 'user', 'get_full_address', 'address', 'postal_code',
                  'province', 'city', 'telephone_number', 'reciever')

        add_fieldsets = (
            'id', 'user', 'postal_code', 'postal_code', 'province', 'city', 'active',
            'telephone_number', 'reciever'
        )
