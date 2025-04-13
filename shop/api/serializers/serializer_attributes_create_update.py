from rest_framework import serializers

from shop.models import (
    AttributeStyle,
    AttributeTech,
    ProductAttributeStyle,
    ProductAttributeTech
)


class AttributeStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeStyle
        fields = ('title', 'position')


class ProductAttributeStyleCreateUpdateSerializer(serializers.ModelSerializer):

    products_tag = AttributeStyleSerializer()

    class Meta:
        model = ProductAttributeStyle
        fields = ('products_tag', 'position')

    def create(self, validated_data):
        products_tag_data = validated_data.pop('products_tag')
        products_tag = AttributeStyle.objects.create(**products_tag_data)
        return ProductAttributeStyle.objects.create(products_tag=products_tag, **validated_data)


class AttributeTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeTech
        fields = ('title',)


class ProductAttributeTechCreateUpdateSerializer(serializers.ModelSerializer):

    products_tag = AttributeTechSerializer()

    class Meta:
        model = ProductAttributeTech
        fields = ('products_tag',)

    def create(self, validated_data):
        products_tag_data = validated_data.pop('products_tag')
        products_tag = AttributeTech.objects.create(**products_tag_data)
        return ProductAttributeTech.objects.create(products_tag=products_tag, **validated_data)
