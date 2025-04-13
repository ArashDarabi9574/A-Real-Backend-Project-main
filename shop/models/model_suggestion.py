from django.db import models


from utils.general.models.model_date_abstract import DateBasic


class Suggestion(DateBasic):
    class Meta:
        verbose_name = 'پیشنهاد محصول'
        verbose_name_plural = 'پیشنهادات محصول'
        ordering = ['primary_product', '-priority']
        unique_together = ('primary_product', 'suggestions')

    primary_product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                        related_name="primary_suggestion", verbose_name='پیشنهاد و ست اصلی')
    suggestions = models.ForeignKey('Product', on_delete=models.CASCADE,
                                    related_name="product_suggestion", verbose_name='سایر پیشنهاد‌ها')
    priority = models.PositiveBigIntegerField(
        default=0, verbose_name='اولیت پیشنهادی این محصول برای کاربر')
