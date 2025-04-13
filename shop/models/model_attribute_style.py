from django.db import models
from django.utils.translation import gettext_lazy as _


class AttributeStyle(models.Model):
    class Meta:
        verbose_name = 'مشخصات کلی'
        verbose_name_plural = 'مشخصات کلی'
        ordering = ['position']

    title = models.CharField(_('نام مشخصه'), max_length=350, null=True, blank=True)
    position = models.PositiveIntegerField(default=0, verbose_name='موقعیت')

    def __str__(self):
        return self.title
