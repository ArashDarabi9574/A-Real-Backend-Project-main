from rest_framework import serializers
from accounts.models import UserAddress


class AddressDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('id', 'user', 'province', 'city', "address",
                  'address', 'postal_code', 'plaque', 'telephone_number', 'reciever')

        add_fieldsets = ('id', 'user', 'province', 'city', 'active',
                         'address', 'postal_code', 'plaque', 'telephone_number', 'reciever')
