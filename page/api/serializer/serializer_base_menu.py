from rest_framework import serializers
from page.models import (
    UpMenu, DownRightMenu, DownLeftMenu, DownMiddleMenu
)

class UpMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpMenu
        fields = '__all__'

class DownRightMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownRightMenu
        fields = '__all__'

class DownLeftMenuerializer(serializers.ModelSerializer):
    class Meta:
        model = DownLeftMenu
        fields = '__all__'

class DownMiddleMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownMiddleMenu
        fields = '__all__'