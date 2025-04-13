from rest_framework import serializers

from shop.api.serializers import BaseProductSerializer
from shop.models import Comment
from accounts.api.serializers.serializer_base_user import BaseUserSerializer


class CommentListSerializer(serializers.ModelSerializer):
    products = BaseProductSerializer(read_only=True)
    user = BaseUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id', 'user', 'status', 'products', 'rate', 'get_created_at_jalali'
        )

        read_only_fields = (
            'id', 'user', 'status', 'products', 'rate', 'get_created_at_jalali'
        )
