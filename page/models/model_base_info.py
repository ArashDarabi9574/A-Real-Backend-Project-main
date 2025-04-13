from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from utils.general.models.model_date_abstract import DateBasic


class BaseInfo(DateBasic):
    class Meta:
        verbose_name = 'اطلاعات ابتدایی'
        verbose_name_plural = verbose_name

    name = models.CharField(max_length=200, verbose_name='نام فروشگاه')
    address = models.CharField(max_length=300, verbose_name='ادرس فروشگاه')
    phone_number = models.CharField(max_length=300, verbose_name='تماس فروشگاه')
    logo = models.ImageField(upload_to='base_info/logo/', verbose_name='لوگو فروشگاه')
    logo_alt = models.CharField(max_length=300, verbose_name='متن در صورت نمایش داده نشدن لوگو')

    def __str__(self):
        return self.name

    def __save__(self, *args, **kwargs):
        if BaseInfo.objects.count() != 0:
            raise ValidationError('There can be only one instance of this model')
        return super().save(*args, **kwargs)
