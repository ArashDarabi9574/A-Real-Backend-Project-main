from rest_framework import serializers

from blog.models.model_blog_post_comment import PostComment
from accounts.api.serializers.serializer_base_user import BaseUserSerializer


class BaseCommentSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer(read_only=True)

    class Meta:
        model = PostComment
        fields = (
            'id', 'user', 'message', 'rate'
        )
        read_only_fields = (
            'id', 'user', 'message'
        )
