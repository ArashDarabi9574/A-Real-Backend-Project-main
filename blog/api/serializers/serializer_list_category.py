from rest_framework import serializers
from blog.api.serializers.serializer_base_category import BaseCategorySerializer
from blog.models.model_blog_post_category import PostCategory


class ListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = (
            'id', 'title',
        )
        read_only_fields = (
            'id', 'title',
        )
