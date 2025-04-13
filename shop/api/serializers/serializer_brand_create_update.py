from rest_framework import serializers
from shop.models import Brand


class BrandCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('title', 'description', 'country',
                  'thumbnail', 'thumbnail_alt', 'position', 'guarantee', 'guarantee_conditions')
