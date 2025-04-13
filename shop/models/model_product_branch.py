from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductBranch(models.Model):
    class Meta:
        verbose_name = 'شعبه'
        verbose_name_plural = 'شعبه‌ها'
        ordering = ['-id']

    branch_product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name='product_branch', verbose_name='شعبه محصولات', null=True)

    branches = models.ForeignKey(
        'Branch', on_delete=models.CASCADE, null=True, blank=True, verbose_name='شعبه')

    inventory = models.PositiveIntegerField(
        default=0, verbose_name='موجودی محصول', null=True, blank=True)

    def branch(self):
        return self.branches.title
