from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

from utils.general.models.model_date_abstract import DateBasic


class ContactUs(DateBasic):
    class Meta:
        verbose_name = _('ارتباط با ما')
        verbose_name_plural = _('ارتباط با ما')
        ordering = ['-created_at']

    phone_number_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_("شماره تلفن درست نیست!"))
    name = models.CharField(_('نام'), max_length=350)
    email = models.EmailField(_('ایمیل'))
    phone_number = models.CharField(_('شماره تلفن'), max_length=11, validators=[phone_number_validator])
    message = RichTextUploadingField(_('نظر'))

    def __str__(self):
        return self.name
