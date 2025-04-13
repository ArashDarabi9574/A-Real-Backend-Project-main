from django.contrib import admin

from shop.models import Discount


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'type_discount', 'type_action', 'percentage',
                    'amount_discount', 'get_created_at_jalali', 'get_updated_at_jalali', 'get_expired_date_jalali',
                    )

    search_fields = ('id', 'code', 'title',
                     'percentage', 'amount_discount')
    list_filter = ('type_discount', 'type_action')
    readonly_fields = ('created_at', 'updated_at',)
    ordering = ['-id', ]

    fieldsets = (
        ('Main', {'fields': ('code', 'title', 'type_discount', 'type_action', 'percentage',
                             'amount_discount',)}),
        ("Date", {'fields': ("expired_date", )}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('code', 'title', 'type_discount', 'type_action', 'percentage',
                             'amount_discount',)}),
        ("Date", {'fields': ("expired_date",)}),
    )
