from django.contrib import admin

from shop.models import Order
from shop.admin.inline_order_item import OrderItemInline


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'description', 'status', 'consistency_code', 'sending_method',
                    'email_sent', 'sms_sent', 'get_created_at_jalali', 'get_updated_at_jalali',
                    'get_complete_date',
                    )
    search_fields = ('id', 'user__id', 'user__phone_number',
                     'user__email', 'consistency_code', 'address__address')
    list_filter = ('user__phone_number', 'user__email',
                   'email_sent', 'sms_sent', 'status', 'sending_method')
    ordering = ['-id', ]
    raw_id_fields = ('user',)
    readonly_fields = ('consistency_code', 'created_at',
                       'updated_at', 'complete_date')
    inlines = [OrderItemInline]

    fieldsets = (
        ('Main', {'fields': ('user', 'description', 'consistency_code',
         'complete_date', 'email_sent', 'sms_sent', 'address')}),
        ("Setting", {'fields': ("status", 'sending_method')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('user', 'description', 'consistency_code',
         'complete_date', 'email_sent', 'sms_sent', 'address')}),
        ("Setting", {'fields': ("status", 'sending_method')}),
    )
