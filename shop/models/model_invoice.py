from django.core.exceptions import ValidationError
from django.db import models

from utils.general.models.model_date_abstract import DateBasic
from shop.models.model_order import Order



class Invoice(DateBasic):
    class Meta:
        verbose_name = "صورتحساب"
        verbose_name_plural = "صورتحساب ها"

    invoice_number = models.CharField(
        unique=True, max_length=128, default=1000, verbose_name="شماره قرارداد")
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name="factors", verbose_name='سبد خرید')

    def __str__(self):
        return str(self.invoice_number)

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                last_obj_id = Invoice.objects.last()
                self.invoice_number = int(last_obj_id.invoice_number) + 1
            except:
                self.invoice_number += 1
        super().save(*args, **kwargs)
