from django.db import models
from django.utils.translation import gettext_lazy as _


class Seo(models.Model):
    class Meta:
        verbose_name = 'سئو'
        verbose_name_plural = 'سئو'
        abstract = True

    meta_title = models.CharField(
        _('عنوان برای سئو'), max_length=320, blank=True, null=True)
    meta_description = models.TextField(
        _('توضیحات برای سئو'), blank=True, null=True)
