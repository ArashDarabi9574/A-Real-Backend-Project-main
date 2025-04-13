from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django_jalali.db import models as jmodels
from model_clone.models import CloneModel
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from utils.general.models.model_date_abstract import DateBasic
from utils.general.models.model_seo_abstract import Seo
from utils.general.models.model_status_abstract import Status
from utils.unique_slug_generator import unique_slug_generator
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from datetime import datetime
from django_jalali.db import models as jmodels
from utils.general.models.model_status_abstract import Choices


class Product(CloneModel, DateBasic, Status, Seo):
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ['status','-updated_at']
        indexes = [
            models.Index(fields=['title']),
        ]
    total_sold = models.BigIntegerField(default=0)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='%(class)s_posts', verbose_name='نویسنده', blank=True, null=True)
    title = models.CharField(_('عنوان'), max_length=128,)
    content = RichTextUploadingField(_('ویژگی‌های اصلی'))
    slug = models.SlugField(unique=True, blank=True)
    thumbnail = models.ImageField(_('تصویر شاخص'),
                                  upload_to=f'thumbnails/{str(datetime.now().year)}/{str(datetime.now().month)}',
                                  blank=True, null=True)
    thumbnail_alt = models.CharField(
        _('متن در صورت نمایش داده نشدن تصویر'), max_length=350, blank=True)
    colors = models.ManyToManyField(
        'Colors', related_name='product_colors', verbose_name='رنگ‌ها', blank=True
    )
    collections = models.ManyToManyField(
        'ProductsCollections', related_name='product_collections', verbose_name='دسته‌بندی‌ها', blank=True
    )
    brand = models.ForeignKey(
        'Brand', related_name='product_brand', verbose_name='برند',
        blank=True, null=True, on_delete=models.CASCADE
    )
    suggestions = models.ManyToManyField('Product', through='Suggestion',
                                         verbose_name="پیشنهادات برای محصول", blank=True)
    main_price = models.PositiveIntegerField(verbose_name='قیمت اصلی محصول')
    price_deadline = models.BooleanField(
        default=False, verbose_name='محصول قیمت موقت دارد؟')
    deadline_price = models.PositiveIntegerField(
        verbose_name='قیمت تخفیف موقت', null=True, blank=True)
    product_review = RichTextUploadingField(
        _('بررسی تخصصی'), blank=True, null=True)
    price_expired_date = models.DateTimeField(null=True,
                                              blank=True, verbose_name="تاریخ میلادی انقضا قیمت")

    price_expired_date_jalali = jmodels.jDateTimeField(null=True,
                                                       blank=True, verbose_name="تاریخ شمسی انقضا قیمت")

    special_tag = models.ManyToManyField(
        'SpecialTag',
        related_name='product_special_tag',
        verbose_name=_('تگ مخصوص'),
        blank=True,
    )
    insurance = models.CharField(default='۷ روز ضمانت بازگشت وجه', null=True,
                                 blank=True, verbose_name="تعداد روز برای ضمانت بازگشت کالا", max_length=256)
    set_watch = models.ForeignKey('self', null=True, blank=True, related_name='product_set_watch',
                                  verbose_name="محصول ست این ساعت", on_delete=models.CASCADE)

    @property
    def get_insurance(self):
        return self.insurance

    def __str__(self):
        return self.title

    @property
    def get_price_expired_date(self):
        if self.price_expired_date:
            return int(self.price_expired_date.timestamp())
        return None

    @property
    def get_price_expired_date_jalali(self):
        if self.price_expired_date_jalali:
            return self.price_expired_date_jalali.strftime('%H:%M - %Y/%m/%d')

    @property
    def get_total_price(self):
        current_date = timezone.now()
        if self.deadline_price:
            if self.price_deadline and self.price_expired_date:
                if current_date > self.price_expired_date:
                    return self.main_price
            return self.deadline_price
        return self.main_price

    @property
    def get_discount_amount(self):
        return int(self.main_price) - int(self.deadline_price)

    @property
    def get_discount_active(self):
        if self.deadline_price:
            if self.deadline_price == self.main_price:
                return False
            return True
        return False

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.price_deadline and self.price_expired_date:
            current_date = timezone.now()
            if current_date > self.price_expired_date:
                self.deadline_price = self.main_price

        super().save(force_insert, force_update, using, update_fields)



@receiver(pre_save, sender=Product)
def pre_product_save_receiver(sender, instance, *args, **kwargs):
    if not instance.thumbnail_alt:
        instance.thumbnail_alt = unique_slug_generator(instance)


@receiver(post_save, sender=Product)
def post_product_save_receiver(sender, instance, created, *args, **kwargs):
    if created and not instance.slug:
        instance.slug = f"az-{instance.id}"
        instance.save()
