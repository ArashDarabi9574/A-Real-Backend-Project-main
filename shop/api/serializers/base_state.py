from rest_framework import serializers
from shop.models import State


class BaseStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'name', 'slug')
