from django.db import models
from django.utils.translation import gettext_lazy as _


class AttributeTech(models.Model):
    class Meta:
        verbose_name = 'مشخصات فنی و تولید'
        verbose_name_plural = 'مشخصات فنی و تولید'
        ordering = ['-id']

    title = models.CharField(
        _('نام مشخصه'), max_length=350, null=True, blank=True)
    position = models.PositiveIntegerField(default=0, verbose_name='موقعیت')

    def __str__(self):
        return self.title
