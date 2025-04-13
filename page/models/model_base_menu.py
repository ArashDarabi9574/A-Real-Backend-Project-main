from django.db import models

from django.utils.translation import gettext_lazy as _


class BaseMenu(models.Model):

    class Meta:
        abstract = True

    title = models.CharField(
        _('عنوان کلید'), max_length=350, blank=True, null=True
    )
    link = models.CharField(
        _('لینک کلید'), max_length=350, blank=True, null=True
    )

    def __str__(self):
        return self.title
