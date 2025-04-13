from rest_framework import serializers

from shop.models import (
    ProductAttributeStyle,
    ProductAttributeTech,
    AttributeStyle
)


class AttributeStyleDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductAttributeStyle
        fields = ('id', 'style', 'content', 'position')
        read_only_fields = ('id', 'style', 'content', 'position')


class AttributeStyleSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttributeStyle
        fields = ('id', 'title', 'position')
        read_only_fields = ('id', 'title', 'position')


class AttributeTechDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeTech
        fields = ('id', 'tech', 'content', 'position')
        read_only_fields = ('id', 'tech', 'content', 'position')
