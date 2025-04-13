from django.contrib import admin

from wallet.models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'balance', 'get_created_at_jalali',
        'user_balance', 'all_users_balance',
    )
    search_fields = ('id', 'user__username')
    raw_id_fields = ('user',)
