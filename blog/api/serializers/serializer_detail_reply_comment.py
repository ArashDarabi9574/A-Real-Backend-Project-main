from rest_framework import serializers

from accounts.api.serializers.serializer_base_user import BaseUserSerializer
from blog.models import PostComment


class PostCommentReplyDetailSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer(read_only=True)

    class Meta:
        model = PostComment
        fields = (
            'id', 'user', 'message', 'rate'
        )
        read_only_fields = (
            'id', 'user', 'message', 'rate'
        )
