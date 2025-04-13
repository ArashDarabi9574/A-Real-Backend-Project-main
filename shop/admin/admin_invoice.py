from django.contrib import admin
from shop.models.model_invoice import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'order')
    search_fields = ('invoice_number',)
    readonly_fields = ('invoice_number',)
    raw_id_fields = ('order',)

    fieldsets = (
        ('Main', {'fields': ('order',)}),

    )

    add_fieldsets = (
        ('Main', {'fields': ('order',)}),

    )
