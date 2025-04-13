from rest_framework import serializers
from blog.models.model_blog_post_comment import PostComment
from blog.api.serializers import BaseCommentSerializer, BasePostSerializer
from accounts.api.serializers.serializer_base_user import BaseUserSerializer


class ListCommentSerializer(serializers.ModelSerializer):
    reply = BaseCommentSerializer()
    post = BasePostSerializer()
    user = BaseUserSerializer(read_only=True)

    class Meta:
        model = PostComment
        fields = (
            'user', 'reply', 'post', 'get_created_at_jalali', 'rate'
        )
        read_only_fields = (
            'user', 'reply', 'post', 'get_created_at_jalali', 'rate'
        )
