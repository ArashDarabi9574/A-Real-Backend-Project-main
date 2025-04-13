from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels


class DateBasic(models.Model):
    class Meta:
        verbose_name = 'تاریخ'
        verbose_name_plural = 'تاریخ‌ها'
        abstract = True

    created_at = models.DateTimeField(_('تاریخ میلادی ساخت'), auto_now_add=True)
    updated_at = models.DateTimeField(_('تاریخ میلادی آپدیت'), auto_now=True)

    created_at_jalali = jmodels.jDateTimeField(_('تاریخ شمسی ساخت'), auto_now_add=True)
    updated_at_jalali = jmodels.jDateTimeField(_('تاریخ شمسی ساخت'), auto_now=True)

    def get_created_at(self):
        return self.created_at.strftime('%H:%M - %Y/%m/%d')

    def get_updated_at(self):
        return self.updated_at.strftime('%H:%M - %Y/%m/%d')

    def get_created_at_jalali(self):
        return self.created_at_jalali.strftime('%H:%M - %Y/%m/%d')

    def get_updated_at_jalali(self):
        return self.updated_at_jalali.strftime('%H:%M - %Y/%m/%d')
