from rest_framework import serializers

from wallet.models import Wallet


class WalletCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = (
            'user', 'balance', 'created_at',
        )
