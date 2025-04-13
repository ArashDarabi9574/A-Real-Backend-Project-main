from django.db import models
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField


class Colors(models.Model):
    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ‌ها'

    color_name = models.CharField(
        max_length=12, blank=True, verbose_name="نام رنگ")
    color = ColorField(_('رنگ'), default='#FF0000')

    def __str__(self):
        return self.color_name
