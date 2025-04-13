from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _
from utils.general.models.model_date_abstract import DateBasic
from utils.general.models.model_seo_abstract import Seo
from utils.general.models.model_basic_post_abstract import BasicPost
from utils.general.models.model_status_public import StatusPublic

from utils.unique_slug_generator import unique_slug_generator


class Post(Seo, BasicPost, DateBasic, StatusPublic):
    class Meta:
        verbose_name = _('پست')
        verbose_name_plural = _('پست‌ها')
        ordering = ['-created_at']

    category = models.ForeignKey('PostCategory', on_delete=models.CASCADE,
                                 related_name='posts',
                                 verbose_name=_('دسته‌بندی'))
    short_description = RichTextUploadingField(_('توضیح کوتاه'))

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Post)
def pre_post_category_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.thumbnail_alt:
        instance.thumbnail_alt = unique_slug_generator(instance)
