from rest_framework import serializers
from page.models import BaseInfo


class BaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseInfo
        fields = ('name', 'address', 'phone_number', 'logo', 'logo_alt')
