from rest_framework import serializers
from blog.models.model_blog_post_category import PostCategory
from blog.api.serializers.serializer_base_category import BaseCategorySerializer


class DetailCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PostCategory
        fields = (
            'id', 'title', 'get_created_at_jalali', 'get_updated_at_jalali', 'get_count_posts',

        )
        read_only_fields = (
            'id', 'title', 'get_created_at_jalali', 'get_updated_at_jalali', 'get_count_posts',
        )
