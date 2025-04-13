from rest_framework import serializers
from shop.models import SpecialTag


class SpecialTagCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialTag
        fields = ('title', 'color')
