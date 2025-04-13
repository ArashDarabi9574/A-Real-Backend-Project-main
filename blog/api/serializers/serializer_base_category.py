from rest_framework import serializers
from blog.models import PostCategory


class BaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = ('id', 'title',)
        read_only_fields = ('id', 'title',)
