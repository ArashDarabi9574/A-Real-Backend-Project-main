from django.db import models
from django.utils.translation import gettext_lazy as _


# class Choices(models.TextChoices):
#     pre_order = _('پیش‌ فروش'), _('پیش‌ فروش')
#     out_stock = _('در انبار موجود نیست'), _('در انبار موجود نیست')
#     in_stock = _('موجود در انبار'), _('موجود در انبار')

class Choices(models.IntegerChoices):
    pre_order = 1, _('پیش‌ فروش')
    out_stock = 2, _('در انبار موجود نیست')
    in_stock = 3, _('موجود در انبار')

class Status(models.Model):
    class Meta:
        verbose_name = 'وضعیت'
        verbose_name_plural = 'وضعیت‌ها'
        abstract = True

    status = models.IntegerField(_('وضعیت'),
                              choices=Choices.choices,
                              default=Choices.in_stock,
                              )
    new_status = models.IntegerField(_('وضعیت'), null=True,choices=Choices.choices, default=Choices.in_stock)
