from django.contrib.auth import get_user_model
from django.db import models
from shop.models import Order
from utils.general.models.model_date_abstract import DateBasic


class Payment(DateBasic):
    class Meta:
        verbose_name = 'پرداخت'
        verbose_name_plural = 'پرداخت‌ها'
        ordering = ['-id']

    class StatusChoices(models.IntegerChoices):
        UnSuccessFull = 0, 'ناموفق'
        SuccessFull = 1, 'موفق'

    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                             null=True, related_name='payments', verbose_name='کاربر')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name='payments',
                              verbose_name='سفارش')

    status = models.PositiveSmallIntegerField(
        null=True, choices=StatusChoices.choices, verbose_name="وضعیت")
    status_code = models.CharField(
        max_length=5, null=True, blank=True, verbose_name="کد وضعیت")
    ref_code = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="کد پیگیری")
    amount = models.PositiveIntegerField(null=True, verbose_name="مبلغ")
    error_message = models.TextField(null=True, blank=True,
                                     verbose_name="پیام ارور", help_text="در صورت بروز خطا")

    def __str__(self):
        if self.user:
            return self.user.phone_number
        return str(self.pk)
