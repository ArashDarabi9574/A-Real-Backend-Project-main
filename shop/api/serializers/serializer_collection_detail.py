from rest_framework import serializers

from shop.models import ProductsCollections
from shop.api.serializers.base_brand import BaseBrandSerializer
from shop.models import Brand


class CollectionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductsCollections
        fields = ('id', 'title', 'slug', 'parent',
                  'position', 'child_position')
        read_only_fields = ('id', 'title', 'slug', 'parent',
                            'position', 'child_position')
        depth = 1
