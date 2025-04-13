from rest_framework import serializers

from shop.models import ProductsCollections
from shop.api.serializers.base_brand import BaseBrandSerializer
from shop.api.serializers.base_collection import BaseCollectionSerializer
from shop.models import Brand


class CollectionListSerializer(serializers.ModelSerializer):
    child_collection = serializers.SerializerMethodField(
        method_name='get_child_collection')

    class Meta:
        model = ProductsCollections
        fields = ('id', 'title', 'slug', 'child_collection',
                  'position')
        read_only_fields = ('id', 'title', 'slug',
                            'child_collection', 'position')

    def get_child_collection(self, obj):
        collection = BaseCollectionSerializer(
            obj.collection_parent.all().order_by('child_position'), many=True)
        return collection.data
