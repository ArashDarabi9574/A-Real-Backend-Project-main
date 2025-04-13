from rest_framework import serializers

from shop.models import ProductsCollections


class BaseCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsCollections
        fields = ('id', 'title', 'slug', 'child_position')
        read_only_fields = ('id', 'title', 'slug',
                            'child_position')
