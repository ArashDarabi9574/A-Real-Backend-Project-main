from django.db import models
from utils.general.models.model_status_public import StatusPublic
from shop.models.model_state import State


class SendingMethod(StatusPublic):
    class Meta:
        verbose_name = "طریقه ارسال محصول"
        verbose_name_plural = "طریقه ارسال محصول"

    title = models.CharField(max_length=255, verbose_name='عنوان')
    description = models.CharField(max_length=500, verbose_name='توضیحات')
    free_price = models.PositiveIntegerField(
        verbose_name='جمع مبلغ خرید چقدر بود هزینه ارسال رایگان شود؟(تومان)', blank=True)
    price = models.IntegerField(
        verbose_name='مبلغ ارسال(تومان)')
    state = models.ManyToManyField(
        State, related_name='sending_methods', verbose_name='استان')

    def __str__(self):
        return self.title

    @property
    def get_state_list(self):
        return ', '.join(str(state.name) for state in self.state.all())
