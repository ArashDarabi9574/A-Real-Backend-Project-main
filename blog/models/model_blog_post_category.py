from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.general.models.model_date_abstract import DateBasic
from blog.models.model_blog_post import Post


class PostCategory(DateBasic):
    class Meta:
        verbose_name = _('دسته‌بندی')
        verbose_name_plural = _('دسته‌بندی‌ها')

        ordering = ['-created_at']
    title = models.CharField(_('عنوان'), max_length=128, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_count_posts(self):
        return Post.objects.filter(category__id=self.id, status='public').count()
