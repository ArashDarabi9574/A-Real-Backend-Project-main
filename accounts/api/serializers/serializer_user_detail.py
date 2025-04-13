from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.api.serializers.serializer_base_address import BaseAddressUpdateSerializer


class UserDetailSerializer(serializers.ModelSerializer):
    address = BaseAddressUpdateSerializer(
        many=True, source='user_address')

    class Meta:
        model = get_user_model()
        add_fieldsets = ['address',]
        exclude = ['password', 'groups', 'user_permissions']
        depth = 1
