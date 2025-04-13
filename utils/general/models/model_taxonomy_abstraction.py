from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


from datetime import datetime


class Taxonomy(models.Model):
    class Meta:
        verbose_name = 'مشخصات'
        verbose_name_plural = 'مشخصات'
        abstract = True

    title = models.CharField(_('عنوان'), max_length=350, null=True, blank=True)
    description = RichTextUploadingField(
        _('توضیحات'), blank=True, null=True)
    slug = models.SlugField(_('slug'), unique=True, blank=True)
    thumbnail = models.ImageField(
        _('تصویر'), upload_to=f'taxonomy/thumbnails/{str(datetime.now().year)}/{str(datetime.now().month)}', blank=True, null=True)
    thumbnail_alt = models.CharField(
        _('متن در صورت نمایش داده نشدن تصویر'), max_length=350, blank=True)
