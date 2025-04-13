from rest_framework import serializers
from shop.models import Brand


class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'title', 'position', 'description', 'country', 'slug', 'thumbnail', 'thumbnail_alt', 'guarantee', 'guarantee_conditions'
                  )
        read_only_fields = ('id', 'title', 'description', 'country', 'slug', 'thumbnail', 'thumbnail_alt', 'guarantee', 'guarantee_conditions'
                            )
