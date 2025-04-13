from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class UserAddress(models.Model):
    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس‌ها'
        ordering = ("-id",)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name='user_address', verbose_name='کاربر')
    province = models.CharField(
        max_length=120, null=True, blank=True, verbose_name="استان")
    city = models.CharField(max_length=120, null=True,
                            blank=True, verbose_name="شهرستان")
    telephone_number = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='شماره تماس')
    reciever = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='نام گیرنده')
    address = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='آدرس منزل')
    postal_code_validator = RegexValidator(
        regex=r'^\d{10}$', message="!کد پستی درست نیست")
    postal_code = models.CharField(max_length=10, blank=True, null=True, validators=[postal_code_validator],
                                   verbose_name='کد پستی')
    plaque = models.CharField(
        max_length=10, blank=True, null=True, verbose_name='پلاک')

    @property
    def get_full_address(self):
        address_parts = [self.province, self.city, self.address, self.plaque]
        full_address = ', '.join(filter(None, address_parts))
        return full_address
