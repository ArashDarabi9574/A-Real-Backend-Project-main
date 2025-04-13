from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from accounts.manager import CustomUserManager


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        ordering = ['-id']

    username = None
    phone_number_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="شماره تلفن درست نیست")
    full_name = models.CharField(max_length=256, null=True, blank=True, verbose_name='نام شما')
    phone_number = models.CharField(unique=True, max_length=16, validators=[phone_number_validator],
                                    verbose_name='شماره تلفن', null=True, blank=True)
    email_validator = RegexValidator(
        regex=r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', message="ایمیل درست نیست")
    email = models.CharField(unique=True, max_length=256, validators=[
                             email_validator], verbose_name='ایمیل', null=True, blank=True)
    verify_date = models.DateTimeField(
        blank=True, null=True, verbose_name='تاریخ تایید حساب')
    address = models.ForeignKey("UserAddress", on_delete=models.CASCADE,
                                related_name='user_address', verbose_name='آدرس', null=True, blank=True)
    national_number = models.CharField(
        unique=True, max_length=16, verbose_name='شماره ملی', null=True, blank=True)
    national_number_validator = RegexValidator(
        regex=r'^\d{10}$', message="شماره ملی درست نیست"),
    is_active = models.BooleanField(
        default=False, verbose_name='حساب کاربر فعال است؟')
    is_verify = models.BooleanField(
        default=False, verbose_name='حساب کاربر تایید شده است')
    permissions = models.ForeignKey("UserPermission", null=True, blank=True, on_delete=models.CASCADE,
                                related_name='user_permission', verbose_name='سطح دسترسی')
    objects = CustomUserManager()
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        try:
            if self.phone_number:
                return str(self.phone_number)
            elif self.email:
                return str(self.email)
        except:
            try:
                str_name = str(self.email)
            except:
                str_name = self.first_name
        return str_name

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_verify_date(self):
        if self.verify_date:
            return self.verify_date.strftime('%H:%M - %Y/%m/%d')
