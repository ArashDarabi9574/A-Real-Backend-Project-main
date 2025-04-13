from django.db import models

from utils.general.models.model_date_abstract import DateBasic
from django.contrib.auth import get_user_model
from django.db.models import Sum, Q
from django.db.models.functions import Coalesce

User = get_user_model()


class Score(DateBasic):
    class Meta:
        verbose_name = 'امتیاز'
        verbose_name_plural = 'امتیازها'

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_score")
    score = models.IntegerField(default=0, null=True,
                                blank=True, verbose_name='امتیاز کاربر')

    @property
    def change_score(self, user, score):
        instance = self.objects.select_for_update().get(user=user)
        if not instance.exists():
            instance = self.objects.create(user=user, score=0)
        else:
            instance = instance.first()
        instance.score += score
        instance.save()
