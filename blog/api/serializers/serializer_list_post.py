from rest_framework import serializers

from blog.models.model_blog_post import Post
from accounts.api.serializers import BaseUserSerializer
from blog.api.serializers import BaseCategorySerializer


class ListPostSerializer(serializers.ModelSerializer):
    author = BaseUserSerializer(read_only=False)
    category = BaseCategorySerializer(read_only=False)

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'slug', 'short_description', 'status', 'thumbnail', 'thumbnail_alt', 'meta_title',
            'meta_description',  'author', 'category', 'get_created_at_jalali', 'get_updated_at_jalali',
        )
        read_only_fields = (
            'id', 'title', 'slug', 'short_description', 'status', 'thumbnail', 'thumbnail_alt', 'meta_title',
            'meta_description',  'author', 'category', 'get_created_at_jalali', 'get_updated_at_jalali',
        )
