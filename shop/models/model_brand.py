from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime

from utils.unique_slug_generator import unique_slug_generator
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class Brand(models.Model):
    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'
        ordering = ['-id']
    title = models.CharField(_('عنوان'), max_length=128)
    description = RichTextUploadingField(
        _('توضیحات'), blank=True, null=True)
    slug = models.SlugField(_('slug'), unique=True, blank=True)
    country = models.CharField(max_length=20,
                               blank=True, null=True, verbose_name='کشور')
    thumbnail = models.ImageField(_('تصویر'),
                                  upload_to=f'thumbnails/{str(datetime.now().year)}/{str(datetime.now().month)}',
                                  blank=True, null=True)
    thumbnail_alt = models.CharField(
        _('متن در صورت نمایش داده نشدن تصویر'), max_length=350, blank=True)
    position = models.PositiveIntegerField(default=0, verbose_name='موقعیت')
    guarantee = models.CharField(null=True,
                                 blank=True, verbose_name="گارانتی", max_length=256)
    guarantee_conditions = RichTextUploadingField(
        _('شرایط گارانتی'), blank=True, null=True)

    @property
    def get_guarantee(self):
        return self.guarantee

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Brand)
def pre_brand_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if not instance.thumbnail_alt:
        instance.thumbnail_alt = unique_slug_generator(instance)
