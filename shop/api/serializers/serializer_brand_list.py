from rest_framework import serializers

from shop.models import Brand


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'title', 'position', 'country', 'slug', 'thumbnail', 'thumbnail_alt'
                  )
        read_only_fields = ('id', 'title', 'country', 'slug', 'thumbnail', 'thumbnail_alt'
                            )
