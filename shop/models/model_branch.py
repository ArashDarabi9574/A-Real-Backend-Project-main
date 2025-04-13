from django.db import models
from django.utils.translation import gettext_lazy as _


class Branch(models.Model):
    class Meta:
        verbose_name = 'شعبه'
        verbose_name_plural = 'شعبه‌ها'
        ordering = ['-id']

    title = models.CharField(_('نام شعبه'), max_length=64)

    def __str__(self):
        return self.title
