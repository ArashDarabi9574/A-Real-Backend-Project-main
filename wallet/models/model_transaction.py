from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from utils.general.models.model_date_abstract import DateBasic
from django.db.models import Sum, Count, Q
from django.db.models.functions import Coalesce
User = get_user_model()


class Transaction(DateBasic):

    class Meta:
        verbose_name = 'تراکنش'
        verbose_name_plural = 'تراکنش‌ها'

    CHARGE = 1
    PURCHASE = 2
    TRANSACTION_TYPE_CHOICES = (
        (CHARGE, "Charge"),
        (PURCHASE, 'Purchase'),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.PositiveSmallIntegerField(
        _('نوع تراکنش'), choices=TRANSACTION_TYPE_CHOICES, default=CHARGE,)
    amount = models.PositiveIntegerField(null=True, verbose_name="مبلغ")

    def __str__(self):
        return f"{self.user} - {self.transaction_type} - {self.amount}"

    @property
    def get_balance(self):
        positive_transactions = Sum(
            'transactions__amount',
            filter=Q(transactions__transactions_type='1')
        )
        negative_transactions = Sum(
            'transactions__amount',
            filter=Q(transactions__transactions_type='2')
        )
        users = User.objects.all().annotate(
            transactions_count=Count('transactions__id'),
            balance=Coalesce(positive_transactions, 0) -
            Coalesce(negative_transactions, 0)
        )
        return users

    @property
    def get_total_balance(self):
        queryset = self.get_balance()
        return queryset.aaggregate(Sum('balance'))
