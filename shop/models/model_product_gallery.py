from django.db import models
from django.utils.translation import gettext_lazy as _

from datetime import datetime


class Gallery(models.Model):
    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'گالری‌ها'

    product_images = models.ForeignKey('Product', on_delete=models.CASCADE,
                                       related_name="images", verbose_name='تصاویر', null=True)
    image = models.ImageField(_('تصویر'),
                              upload_to=f'basic_gallery/images/{str(datetime.now().year)}/{str(datetime.now().month)}', blank=True)
    image_alt = models.CharField(
        _('متن در صورت نمایش داده نشدن تصویر'), max_length=350, blank=True)

    def __str__(self) -> str:
        return self.image_alt
