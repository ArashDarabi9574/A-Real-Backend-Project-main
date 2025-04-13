from django.db import models
from django.utils.translation import gettext_lazy as _

from datetime import datetime


class Slider(models.Model):
    class Meta:
        verbose_name = 'تصویر اسلایدر'
        verbose_name_plural = 'تصایر اسلایدر'
        ordering = ('position',)

    sliders = models.ForeignKey('LandingPage', on_delete=models.CASCADE,
                                related_name="sliders", verbose_name='اسلاید‌ها', null=True)
    slider_image = models.ImageField(_('تصویر اسلایدر'),
                                     upload_to=f'landing_images/sliders/{str(datetime.now().year)}/{str(datetime.now().month)}', blank=True)
    slider_image_alt = models.CharField(
        _('متن در صورت نمایش داده نشدن تصویر'), max_length=350, blank=True)
    slider_link = models.URLField(_('لینک اسلایدر'), null=True)    
    position = models.PositiveIntegerField(default=0, verbose_name='موقعیت')

    def __str__(self):
        return self.slider_link


class Icons(models.Model):
    class Meta:
        verbose_name = 'آیکون'
        verbose_name_plural = 'آیکون‌ها'
        ordering = ('position',)

    icons = models.ForeignKey('LandingPage', on_delete=models.CASCADE,
                              related_name="icons", verbose_name='آیکون‌ها', null=True)
    icon_thumbnail = models.ImageField(_('تصویر آیکون'),
                                       upload_to=f'landing_images/icons/{str(datetime.now().year)}/{str(datetime.now().month)}', blank=True)
    icon_thumbnail_alt = models.CharField(
        _('متن در صورت نمایش داده نشدن تصویر'), max_length=350, blank=True)
    icon_link = models.URLField(_('لینک آیکون'), null=True)
    icon_name = models.CharField(_('نام آیکون'), max_length=64, blank=True)    
    position = models.PositiveIntegerField(default=0, verbose_name='موقعیت')

    def __str__(self):
        return self.icon_name


class UnderSlider(models.Model):
    class Meta:
        verbose_name = 'تصویر زیر اسلایدر'
        verbose_name_plural = 'تصاویر زیر اسلایدر'
        ordering = ('position',)
    under_slider = models.ForeignKey('LandingPage', on_delete=models.CASCADE,
                                     related_name="under_slider", verbose_name='تصاویر زیر اسلایدر', null=True)
    under_slider_image = models.ImageField(_('تصویر زیر اسلیدر'),
                                           upload_to=f'landing_images/under_slider{str(datetime.now().year)}/{str(datetime.now().month)}',
                                           blank=True, null=True)
    under_slider_image_alt = models.CharField(
        _('متن در صورت نمایش داده نشدن تصویر'), max_length=350, blank=True)

    under_slider_link = models.CharField(
        _('لینک کلید'), max_length=350, blank=True, null=True
    )
    
    position = models.PositiveIntegerField(default=0, verbose_name='موقعیت')

