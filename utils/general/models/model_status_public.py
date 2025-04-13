from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusPublic(models.Model):
    class Meta:
        abstract = True

    class Choices(models.IntegerChoices):
        publish = 0, _('منتشر شده')
        archive = 1, _('آرشیو شده')
        pending = 2, _('پیش‌نویس‌ها')

    status = models.IntegerField(_('وضعیت'),
                              choices=Choices.choices,
                              default=Choices.pending,
                              )
