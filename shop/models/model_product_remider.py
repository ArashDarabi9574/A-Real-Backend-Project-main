from accounts.models import CustomUser

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from datetime import datetime


class ProductRemider(models.Model):
    class Meta:
        verbose_name = 'موجود شد خبر بده'
        verbose_name_plural = 'موجود شد خبر بده'

    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                related_name="remiders_product", verbose_name='محصول', null=True)
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                            related_name="remiders_user", verbose_name='محصول', null=True)

    def __str__(self) -> str:
        return str(self.id)
    
    def save(self, *args, **kwargs):
        # Check if a record with the same user and product already exists
        if ProductRemider.objects.filter(user=self.user, product=self.product).exists():
            raise ValidationError("A reminder already exists for this user and product.")
        
        super().save(*args, **kwargs)