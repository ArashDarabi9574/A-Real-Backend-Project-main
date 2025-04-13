from django.contrib import admin

from shop.models import OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem

    fieldsets = (
        ('Main', {'fields': ('products', 'orders', 'branches')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('products', 'orders', 'branches')}),
    )
