from rest_framework import serializers

from shop.models import Product


class SetWatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'thumbnail', 'thumbnail_alt')
        read_only_fields = ('id', 'title', 'slug',
                            'thumbnail', 'thumbnail_alt')
