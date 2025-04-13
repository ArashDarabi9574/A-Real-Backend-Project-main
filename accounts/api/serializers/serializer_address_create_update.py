from rest_framework import serializers
from accounts.models import UserAddress


class AddressCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('province', 'city',
                  'address', 'postal_code', 'plaque', 'telephone_number', 'reciever')
