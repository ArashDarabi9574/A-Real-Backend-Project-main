from django.db import models

from utils.general.models.model_date_abstract import DateBasic
from django.contrib.auth import get_user_model
from django.db.models import Sum, Q
from django.db.models.functions import Coalesce


User = get_user_model()


class Wallet(DateBasic):
    class Meta:
        verbose_name = 'کیف پول'
        verbose_name_plural = 'کیف پول'

    user = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name='balance_stock')
    balance = models.IntegerField(default=0, null=True,
                                  blank=True, verbose_name='موجودی کیف پول')

    def __str__(self):
        return f"{self.user} - {self.balance} - {self.created_at_jalali}"

    @property
    def user_balance(self, user):
        positive_transactions = Sum('amount', filter=Q(transaction_type='1'))
        negative_transactions = Sum(
            'amount', filter=Q(transaction_type__in='2'))

        user_balance = user.transactions.all().aggregate(
            balance=Coalesce(positive_transactions, 0) -
            Coalesce(negative_transactions, 0)
        )

        instance = self.objects.create(
            user=user, balance=user_balance['balance'])
        return instance

    @property
    def all_users_balance(cls):
        for user in User.objects.all():
            record = cls.user_balance(user)
