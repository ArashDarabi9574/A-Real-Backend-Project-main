from rest_framework import serializers
from blog.models.model_blog_post_comment import PostComment

from accounts.api.serializers.serializer_base_user import BaseUserSerializer
from blog.api.serializers.serializer_detail_reply_comment import PostCommentReplyDetailSerializer


class DetailCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    user = BaseUserSerializer(read_only=True)

    class Meta:
        model = PostComment
        fields = (
            'id', 'user', 'message', 'replies', 'get_created_at_jalali', 'rate'
        )
        read_only_fields = (
            'id', 'user', 'message', 'replies', 'get_created_at_jalali', 'rate'
        )

    def get_replies(self, obj):
        replies = PostComment.objects.filter(
            reply=obj, is_reply=True)

        if replies:
            return PostCommentReplyDetailSerializer(replies, many=True, read_only=True).data
        return []
