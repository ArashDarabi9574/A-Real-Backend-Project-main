from rest_framework import serializers
from shop.models import Colors


class ColorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ('id', 'color_name', 'color')
        read_only_fields = ('id', 'color_name', 'color')
