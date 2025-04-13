from rest_framework import serializers
from shop.models import Colors


class ColorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ('id', 'color_name')
        read_only_fields = ('id', 'color_name')
