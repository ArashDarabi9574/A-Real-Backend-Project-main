from django.db import models
from django.utils.translation import gettext_lazy as _
from forms.models.model_base_comment_abstract import BaseComment
from utils.general.models.model_date_abstract import DateBasic

from blog.models.model_blog_post import Post


class PostComment(BaseComment, DateBasic):
    class Meta:
        verbose_name = _('نظر')
        verbose_name_plural = _('نظرات')
        ordering = ['-created_at']

    reply = models.ForeignKey('self', on_delete=models.CASCADE,
                              related_name='post_comments_reply', verbose_name=_('پاسخ'),
                              blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments',
                             verbose_name=_('نظر'))
    is_reply = models.BooleanField(
        default=False, verbose_name='جواب پیام است ؟')

    def __str__(self):
        return str(self.id)
