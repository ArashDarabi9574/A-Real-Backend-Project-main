from django.db import models
from django.utils.translation import gettext_lazy as _


class LanguageStatus(models.Model):
    class Meta:
        verbose_name = 'زبان'
        verbose_name_plural = 'زبان‌ها'
        abstract = True

    is_active = models.BooleanField(_('فعال کردن چند زبانه شدن'), default=False)
