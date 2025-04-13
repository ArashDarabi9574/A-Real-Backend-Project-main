from rest_framework import serializers

from shop.models import ProductRemider
from shop.api.serializers.base_products import BaseProductSerializer


class BaseProductRemiderSerializer(serializers.ModelSerializer):
    product = BaseProductSerializer(read_only=True)

    class Meta:
        model = ProductRemider
        fields = ('id', 'product')
        depth = 1


class CreateProductRemiderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductRemider
        fields = ('product',)
