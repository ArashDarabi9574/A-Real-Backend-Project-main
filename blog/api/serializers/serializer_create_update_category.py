from rest_framework import serializers
from blog.models.model_blog_post_category import PostCategory


class CreateUpdateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = (
            'id', 'title',
        )
