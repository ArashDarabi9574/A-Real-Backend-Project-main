from rest_framework import serializers
from blog.models.model_blog_post import Post
from blog.api.serializers import BaseCategorySerializer
from accounts.api.serializers import BaseUserSerializer
from blog.models import PostComment
from blog.api.serializers.serializer_detail_comment import DetailCommentSerializer


class DetailPostSerializer(serializers.ModelSerializer):
    category = BaseCategorySerializer(read_only=True)
    author = BaseUserSerializer(read_only=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'content', 'slug', 'thumbnail', 'thumbnail_alt',
            'author', 'category', 'get_created_at_jalali', 'get_updated_at_jalali',
            'meta_title', 'meta_description', 'short_description', 'comments',
            'status',
        )

        read_only_fields = (
            'id', 'title', 'content', 'slug', 'thumbnail', 'thumbnail_alt',
            'author', 'category', 'get_created_at_jalali', 'get_updated_at_jalali',
            'meta_title', 'meta_description', 'short_description', 'comments',
            'status',
        )

    def get_comments(self, obj):
        top_level_comments = PostComment.objects.filter(
            post=obj, is_reply=False)
        if top_level_comments:
            return DetailCommentSerializer(top_level_comments, many=True, read_only=True).data
        return []
