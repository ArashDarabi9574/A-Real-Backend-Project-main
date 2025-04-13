from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from utils.unique_slug_generator import unique_slug_generator


class ProductsCollections(models.Model):
    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'
        ordering = ['-id']

    title = models.CharField(_('عنوان'), max_length=64)
    position = models.PositiveIntegerField(default=0, verbose_name='موقعیت')
    child_position = models.PositiveIntegerField(
        default=0, verbose_name='موقعیت زیردسته', null=True, blank=True)

    slug = models.SlugField(_('slug'), unique=True, blank=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name="collection_parent", verbose_name='دسته بندی مادر',
                               null=True, blank=True)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=ProductsCollections)
def pre_product_collections_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
