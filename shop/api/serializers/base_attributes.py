from rest_framework import serializers

from shop.models import (
    ProductAttributeStyle,
    ProductAttributeTech
)


class BaseAttributeStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeStyle
        fields = ('style', 'content', 'position')


class BaseAttributeTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeTech
        fields = ('tech', 'content', 'position')
