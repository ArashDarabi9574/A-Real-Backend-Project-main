from rest_framework import serializers

from wallet.models import Wallet
from accounts.api.serializers.serializer_base_user import BaseUserSerializer


class WalletListSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer(read_only=True)

    class Meta:
        model = Wallet
        fields = (
            'id', 'user', 'balance', 'user_balance', 'all_users_balance'
        )
        read_only_fields = (
            'id', 'user', 'user_balance', 'all_users_balance'
        )
