from rest_framework import serializers

from shop.models import ProductsCollections


class CollectionCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsCollections
        fields = ('title', 'parent', 'slug', 'position', 'child_position')
