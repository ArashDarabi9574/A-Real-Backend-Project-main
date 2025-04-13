from rest_framework import serializers

from shop.models import Brand


class BaseBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('id', 'title', 'country', 'position', 'guarantee', 'guarantee_conditions')
        read_only_fields = ('id', 'title', 'country', 'position', 'guarantee', 'guarantee_conditions')
