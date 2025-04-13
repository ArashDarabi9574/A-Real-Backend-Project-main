from django.contrib import admin

from wallet.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'transaction_type', 'amount', 'get_created_at_jalali'
    )
    list_filter = ('transaction_type',)
    search_fields = ('id', 'user__username')
    raw_id_fields = ('user',)
