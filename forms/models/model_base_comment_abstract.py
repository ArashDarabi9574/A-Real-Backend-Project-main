from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from utils.general.models.model_date_abstract import DateBasic


class BaseComment(DateBasic):
    class Meta:
        abstract = True

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             verbose_name='کاربر', related_name='%(class)s_comments', null=True)
    rate = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1, 'امتیاز باید حداقل 1 باشد.'),
        MaxValueValidator(5, 'امتیاز باید حداکثر 5 باشد.')],
        verbose_name='امتیاز')
    message = models.TextField(_('نظر'))
