from django.db import models

from django.utils.translation import gettext_lazy as _


class ProductAttributeTech(models.Model):
    class Meta:
        verbose_name = 'مشخصات فنی و تولید'
        verbose_name_plural = 'مشخصات فنی و تولید'
        ordering = ['-id']

    products = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name='product_tech_attr', verbose_name='محصولات', null=True)
    products_tag = models.ForeignKey(
        'AttributeTech', on_delete=models.CASCADE, null=True, blank=True, verbose_name='مشخصه فنی و تولید')

    content = models.CharField(
        _('توضیحات'), max_length=350, null=True, blank=True)

    position = models.PositiveIntegerField(default=0, verbose_name='موقعیت')

    @property
    def tech(self):
        return self.products_tag.title
