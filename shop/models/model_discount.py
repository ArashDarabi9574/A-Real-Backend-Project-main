from django.db import models
from django_jalali.db import models as jmodels

from utils.general.models.model_date_abstract import DateBasic
from utils.generator import generate_code


class Discount(DateBasic):
    class Meta:
        verbose_name = 'تخفیف'
        verbose_name_plural = 'تخفیف‌ها'
        ordering = ['-id']

    class TypeDiscount(models.IntegerChoices):
        Percentage = 0, 'درصدی'
        Stable = 1, 'ثابت'

    class TypeAction(models.IntegerChoices):
        Single = 0, 'تکی'
        Overall = 1, 'همگانی'

    code = models.CharField(max_length=20, unique=True,
                            null=True, blank=True, verbose_name='کد تخفیف')
    title = models.CharField(max_length=350, verbose_name='عنوان تخفیف')
    type_discount = models.PositiveSmallIntegerField(choices=TypeDiscount.choices,
                                                     verbose_name="نوع تخفیف")
    type_action = models.PositiveSmallIntegerField(
        choices=TypeAction.choices, verbose_name="نوع اعمال")
    percentage = models.IntegerField(default=0, null=True,
                                     blank=True, verbose_name="درصد تخفیف")
    amount_discount = models.IntegerField(default=0, null=True,
                                          blank=True, verbose_name="مبلغ تخفیف")

    expired_date = models.DateTimeField(null=True,
                                        blank=True, verbose_name="تاریخ میلادی انقضا کد")
    expired_date_jalali = jmodels.jDateTimeField(null=True,
                                                 blank=True, verbose_name="تاریخ شمسی انقضا کد")

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.code:
            self.code = generate_code(length=20, number=True, character=True)
        super().save(force_insert, force_update, using, update_fields)

    @property
    def get_expired_date(self):
        if self.expired_date:
            return self.expired_date.strftime('%H:%M - %Y/%m/%d')

    @property
    def get_expired_date_jalali(self):
        if self.expired_date_jalali:
            return self.expired_date_jalali.strftime('%H:%M - %Y/%m/%d')
