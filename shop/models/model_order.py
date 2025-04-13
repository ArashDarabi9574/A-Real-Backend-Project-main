from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum, ExpressionWrapper, F, fields
from django.utils import timezone
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from accounts.models import UserAddress
from shop.models.model_order_item import OrderItem
from shop.models.model_discount import Discount
from utils.general.models.model_date_abstract import DateBasic
from utils.generator import generate_code
from shop.models.model_sending_method import SendingMethod


class Order(DateBasic):
    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'
        ordering = ("-id",)

    class StatusChoice(models.IntegerChoices):
        AwaitingPayment = 0, "در انتظار پرداخت"
        DoingPayment = 1, "پرداخت موفق"
        SuccessfulPayment = 2, "در حال انجام"
        CompletePayment = 3, "تکمیل شده"
        CanceledPayment = 4, "مرجوع شده"

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name='user_orders', verbose_name='کاربر')
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name="توضحیات")
    status = models.IntegerField(
        _('وضعیت'), choices=StatusChoice.choices, default=StatusChoice.AwaitingPayment,)
    sending_method = models.ForeignKey(SendingMethod, on_delete=models.CASCADE, related_name='orders',
                                       verbose_name="روش ارسال")
    consistency_code = models.CharField(max_length=156, blank=True, unique=True, verbose_name="کد پیگیری سفارش")

    email_sent = models.BooleanField(default=False, verbose_name="ارسال ایمیل")
    sms_sent = models.BooleanField(default=False, verbose_name="ارسال پیامک")
    complete_date = models.DateTimeField(
        null=True, blank=True, verbose_name='زمان تکمیل خرید')
    payment_method = models.CharField(max_length=156, blank=True, verbose_name="متد پرداخت")
    discount = models.ForeignKey(Discount, null=True, blank=True, verbose_name="کد تخفیف", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.consistency_code}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.consistency_code:
            self.consistency_code = generate_code(
                length=12, number=True, character=True)

        if self.status == 3 and not self.complete_date:
            self.complete_date = timezone.now()
        super().save(force_insert, force_update, using, update_fields)

    @property
    def get_complete_date(self):
        if self.complete_date:
            return self.complete_date.strftime('%H:%M - %Y/%m/%d')
        return None

    @property
    def get_total_price(self):
        total_price = OrderItem.objects.filter(orders_id=self.pk).aggregate(
            total_price=ExpressionWrapper(
                Sum(F('paid_price') * F('quantity')),
                output_field=fields.IntegerField()))['total_price'] or 0

        sending_price = self.sending_method.price
        if self.sending_method.free_price != 0 and total_price > self.sending_method.free_price:
            sending_price = 0
        return total_price + sending_price
