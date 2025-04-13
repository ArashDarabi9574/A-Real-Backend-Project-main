from django.db import models

from django.utils.translation import gettext_lazy as _
from datetime import datetime


class LandingPage(models.Model):

    class Meta:
        verbose_name = 'مدیریت صفحه‌اصلی'
        verbose_name_plural = 'مدیریت صفحات اصلی'
        ordering = ['-id']

    landing_page_name = models.CharField(
        _('عنوان کلید'), max_length=128, blank=True)

    button_image = models.ImageField(_('تصویر پایین صفحه'),
                                     upload_to=f'landing_images/{str(datetime.now().year)}/{str(datetime.now().month)}',
                                     blank=True, null=True)
    button_image_alt = models.CharField(
        _('متن در صورت نمایش داده نشدن تصویر'), max_length=350, blank=True, null=True)
    button_link = models.CharField(
        _('لینک کلید'), max_length=350, blank=True, null=True
    )
    quick_access_name = models.CharField(
        _('متن کلید دسترسی سریع'), max_length=350, blank=True, null=True
    )
    quick_access_link = models.CharField(
        _('لینک کلید دسترسی سریع'), max_length=350, blank=True, null=True
    )

    special_link_1 = models.CharField(
        _('لینک کلید پیشنهاد ویژه ۱'), max_length=350, blank=True, null=True
    )
    special_image_1 = models.ImageField(_('تصویر پیشنهاد ویژه ۱'),
                                     upload_to=f'landing_images/{str(datetime.now().year)}/{str(datetime.now().month)}',
                                     blank=True, null=True)
    special_title_1 = models.CharField(
        _('تایتل پیشنهاد ویژه ۱'), max_length=350, blank=True, null=True
    )
    special_desc_1 = models.CharField(
        _('توضیحات پیشنهاد ویژه ۱'), max_length=350, blank=True, null=True
    )

    ########################################################################

    special_link_2 = models.CharField(
        _('لینک کلید پیشنهاد ویژه ۲'), max_length=350, blank=True, null=True
    )
    special_image_2 = models.ImageField(_('تصویر پیشنهاد ویژه ۲'),
                                     upload_to=f'landing_images/{str(datetime.now().year)}/{str(datetime.now().month)}',
                                     blank=True, null=True)
    special_title_2 = models.CharField(
        _('تایتل پیشنهاد ویژه ۲'), max_length=350, blank=True, null=True
    )
    special_desc_2 = models.CharField(
        _('توضیحات پیشنهاد ویژه ۲'), max_length=350, blank=True, null=True
    )

    ########################################################################

    special_link_3 = models.CharField(
        _('لینک کلید پیشنهاد ویژه ۳'), max_length=350, blank=True, null=True
    )
    special_image_3 = models.ImageField(_('تصویر پیشنهاد ویژه ۳'),
                                     upload_to=f'landing_images/{str(datetime.now().year)}/{str(datetime.now().month)}',
                                     blank=True, null=True)
    special_title_3 = models.CharField(
        _('تایتل پیشنهاد ویژه ۳'), max_length=350, blank=True, null=True
    )
    special_desc_3 = models.CharField(
        _('توضیحات پیشنهاد ویژه ۳'), max_length=350, blank=True, null=True
    )

    ########################################################################



    def __str__(self):
        return self.landing_page_name
