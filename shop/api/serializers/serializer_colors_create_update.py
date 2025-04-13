from rest_framework import serializers
from shop.models import Colors


class ColorCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ('color_name', 'color')
