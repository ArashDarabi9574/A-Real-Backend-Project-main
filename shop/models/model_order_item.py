from django.db import models

from utils.general.models.model_date_abstract import DateBasic


class OrderItem(DateBasic):
    class Meta:
        verbose_name = 'محصول سفارش'
        verbose_name_plural = 'محصولات سفارش'
        ordering = ("-orders", "-created_at")

    orders = models.ForeignKey(
        "Order", on_delete=models.CASCADE, related_name="order_items", verbose_name="شناسه سفارش")
    products = models.ForeignKey("Product", on_delete=models.SET_NULL,
                                 null=True, verbose_name="محصول", related_name="product_items")
    quantity = models.PositiveSmallIntegerField(
        default=1, verbose_name="تعداد سفارش")
    main_price = models.PositiveIntegerField(
        null=True, blank=True, default=0, verbose_name='هزینه‌ی اصلی')
    paid_price = models.PositiveIntegerField(
        null=True, blank=True, default=0, verbose_name='هزینه‌ی پرداختی')
    branches = models.ForeignKey("Branch", on_delete=models.CASCADE,
                                 related_name='branch_items', verbose_name='شعبه')

    def __str__(self) -> str:
        return str(self.pk)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.main_price = self.paid_price = self.products.get_total_price
        self.products.total_sold += 1
        self.products.save()

        super().save(force_insert, force_update, using, update_fields)
