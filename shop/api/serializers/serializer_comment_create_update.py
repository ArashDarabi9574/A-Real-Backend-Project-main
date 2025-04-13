from rest_framework import serializers

from shop.models import Comment


class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'message', 'status', 'products', 'rate',
        )
