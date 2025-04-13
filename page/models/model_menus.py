from .model_base_menu import BaseMenu
from django.db import models


class UpMenu(BaseMenu):
    class Meta:
        verbose_name = 'منوی دسته بندی هدر'
        verbose_name_plural = 'منوی دسته بندی هدر'
        ordering = ('position',)

    landing = models.ForeignKey('LandingPage', on_delete=models.CASCADE,
                                related_name="up_menu", verbose_name='لندینگ', null=True)
    description = models.CharField(max_length=256, null=True, blank=True, verbose_name="توضیحات")
    position = models.PositiveIntegerField(default=0, verbose_name='موقعیت')


class DownRightMenu(BaseMenu):
    class Meta:
        verbose_name = 'منوی راست فوتر'
        verbose_name_plural = 'منوی راست فوتر'
        ordering = ('position',)
        
    landing = models.ForeignKey('LandingPage', on_delete=models.CASCADE,
                                related_name="down_right_menu", verbose_name='لندینگ', null=True)
    position = models.PositiveIntegerField(default=0, verbose_name='موقعیت')

class DownMiddleMenu(BaseMenu):
    class Meta:
        verbose_name = 'منوی وسط فوتر'
        verbose_name_plural = 'منوی وسط فوتر'
        ordering = ('position',)
        
    landing = models.ForeignKey('LandingPage', on_delete=models.CASCADE,
                                related_name="down_middle_menu", verbose_name='لندینگ', null=True)
    position = models.PositiveIntegerField(default=0, verbose_name='موقعیت')

class DownLeftMenu(BaseMenu):
    class Meta:
        verbose_name = 'منوی چپ فوتر'
        verbose_name_plural = 'منوی چپ فوتر'
        ordering = ('position',)
        
    landing = models.ForeignKey('LandingPage', on_delete=models.CASCADE,
                                related_name="down_left_menu", verbose_name='لندینگ', null=True)
    position = models.PositiveIntegerField(default=0, verbose_name='موقعیت')