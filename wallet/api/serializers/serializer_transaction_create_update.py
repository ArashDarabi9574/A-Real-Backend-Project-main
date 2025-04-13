from rest_framework import serializers

from wallet.models import Transaction


class TransactionCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'user', 'transaction_type', 'amount', 'created_at',
        )
