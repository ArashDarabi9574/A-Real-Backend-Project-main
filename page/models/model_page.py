from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from utils.general.models.model_seo_abstract import Seo
from utils.general.models.model_date_abstract import DateBasic
from ckeditor_uploader.fields import RichTextUploadingField
from utils.unique_slug_generator import unique_slug_generator


class Page(Seo, DateBasic):
    class Meta:
        verbose_name = _('صفحه')
        verbose_name_plural = _('صفحه‌ها')
        ordering = ['-created_at']
    title = models.CharField(_('عنوان'), max_length=64, null=True, blank=True)
    content = RichTextUploadingField(_('محتوا'))
    slug = models.SlugField(unique=True, blank=True)
    custom_template = models.BooleanField(
        _('نمونه شخصی‌سازی شده'), default=False)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Page)
def page_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
