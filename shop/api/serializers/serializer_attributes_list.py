from rest_framework import serializers

from shop.models import (
    ProductAttributeStyle,
    ProductAttributeTech
)


class AttributeStyleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeStyle
        fields = ('id', 'style', 'position')
        read_only_fields = ('id', 'style', 'position')


class AttributeTechListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeTech
        fields = ('id', 'tech', 'position')
        read_only_fields = ('id', 'tech', 'position')
