from rest_framework import serializers
from blog.models.model_blog_post import Post


class BasePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 'title', 'slug', 'author', 'category'
        )
        read_only_fields = (
            'id', 'title', 'slug', 'author', 'category'
        )
