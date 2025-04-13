from django.db import models

from django.utils.translation import gettext_lazy as _


class ProductAttributeStyle(models.Model):
    class Meta:
        verbose_name = 'مشخصات کلی'
        verbose_name_plural = 'مشخصات کلی'
        ordering = ['products_tag__position']

    products = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name='product_tags', verbose_name='محصولات', null=True)
    products_tag = models.ForeignKey(
        'AttributeStyle', on_delete=models.CASCADE, null=True, blank=True, verbose_name='مشخصه')

    content = models.CharField(
        _('توضیحات'), max_length=350, null=True, blank=True)

    position = models.PositiveIntegerField(default=0, verbose_name='موقعیت')

    @property
    def style(self):
        return self.products_tag.title
