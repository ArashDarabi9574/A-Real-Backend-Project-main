from django.db import models
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField


class SpecialTag(models.Model):
    class Meta:
        verbose_name = 'تگ ویژه'
        verbose_name_plural = 'تگ‌های ویژه'
        ordering = ['-id']

    title = models.CharField(_('عنوان'), max_length=64)
    color = ColorField(_('رنگ'), default='#FF0000')

    def __str__(self) -> str:
        return self.title
