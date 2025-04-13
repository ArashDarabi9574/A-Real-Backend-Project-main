from rest_framework import serializers

from shop.models.model_comment import Comment
from accounts.api.serializers.serializer_base_user import BaseUserSerializer


class BaseProductCommentSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id', 'user', 'message', 'rate', 'get_created_at_jalali'
        )
        read_only_fields = (
            'id', 'user', 'message', 'rate', 'get_created_at_jalali'
        )
