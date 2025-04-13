from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from forms.models.model_base_comment_abstract import BaseComment
from utils.general.models.model_date_abstract import DateBasic
from django.utils.translation import gettext_lazy as _


class Comment(BaseComment, DateBasic):

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
        ordering = ['-id']

    class Choices(models.TextChoices):
        pending = _('در انتظار تأیید'), _('در انتظار تأیید')
        publish = _('منتشر شده'), _('منتشر شده')

    status = models.CharField(_('وضعیت'),
                              max_length=32,
                              choices=Choices.choices,
                              default=Choices.pending,
                              )
    products = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name='product_comments', verbose_name='محصولات')

    def __str__(self):
        return str(self.id)
