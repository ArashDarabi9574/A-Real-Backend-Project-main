from django.contrib import admin

from shop.models import OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'products', 'orders', 'main_price', 'paid_price',
                    'branches', 'quantity', 'get_created_at_jalali', 'get_updated_at_jalali'
                    )

    search_fields = ('id', 'products__title',
                     'orders__consistency_code', 'orders__user__phone_number')
    list_filter = ('orders__user__id', 'orders__id', 'products__title')
    ordering = ['-id', ]
    raw_id_fields = ('products', 'orders')
    readonly_fields = ('main_price', 'paid_price', 'created_at', 'updated_at')

    fieldsets = (
        ('Main', {'fields': ('products', 'orders',
         'main_price', 'paid_price', 'quantity')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('products', 'orders',
         'main_price', 'paid_price', 'quantity')}),
    )
