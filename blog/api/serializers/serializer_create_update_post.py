from rest_framework import serializers
from blog.models.model_blog_post import Post


class CreateUpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 'title', 'content', 'slug', 'thumbnail', 'thumbnail_alt', 'status',
            'category', 'meta_title', 'meta_description', 'short_description'
        )
