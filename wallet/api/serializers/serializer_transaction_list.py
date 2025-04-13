from rest_framework import serializers

from wallet.models import Transaction


class TransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'id', 'user', 'transaction_type', 'amount', 'get_balance',
            'get_total_balance', 'get_created_at', 'get_created_at_jalali'
        )
        read_only_fields = (
            'id', 'user', 'get_balance', 'get_total_balance', 'get_created_at', 'get_created_at_jalali'
        )
