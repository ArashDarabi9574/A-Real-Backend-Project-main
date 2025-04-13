from rest_framework import serializers
from shop.models import SpecialTag


class SpecialTagDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecialTag
        fields = ('id', 'title', 'color')
        read_only_fields = ('id', 'title', 'color')
