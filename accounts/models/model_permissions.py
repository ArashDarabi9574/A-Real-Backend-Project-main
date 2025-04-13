from django.db import models


class UserPermission(models.Model):
    name = models.CharField(max_length=120, null=True, verbose_name="عنوان سطح دسترسی")
    blog_access = models.BooleanField(default=False, verbose_name='دسترسی بلاگ')
    product_access = models.BooleanField(default=False, verbose_name='دسترسی محصولات')
    order_access = models.BooleanField(default=False, verbose_name='دسترسی سفارشات')
    client_access = models.BooleanField(default=False, verbose_name='دسترسی کاربران')
    user_access = models.BooleanField(default=False, verbose_name='دسترسی همکاران')
    
    class Meta:
        verbose_name = 'دسترسی'
        verbose_name_plural = 'دسترسی‌ها'
        ordering = ("-id",)
    
    def __str__(self) -> str:
        return self.name