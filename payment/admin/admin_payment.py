from django.contrib import admin

from payment.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'order', 'user', 'status', 'status_code', 'ref_code',
        'amount', 'error_message', 'get_created_at', 'get_updated_at',
    )

    list_filter = ('order', 'user', 'status', 'status_code',)
    search_fields = ('id', 'order', 'user', 'ref_code', 'error_message')
    readonly_fields = ('created_at', 'updated_at')
    raw_id_fields = ('user', 'order')

    fieldsets = (
        ('Main', {'fields': ('order', 'user', 'status',
         'status_code', 'ref_code', 'amount', 'error_message')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('order', 'user', 'status',
         'status_code', 'ref_code', 'amount', 'error_message')}),
    )
