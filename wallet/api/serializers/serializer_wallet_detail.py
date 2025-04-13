from rest_framework import serializers

from wallet.models import Wallet
from accounts.api.serializers.serializer_base_user import BaseUserSerializer


class WalletDetailSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer(read_only=True)

    class Meta:
        model = Wallet
        fields = (
            'id', 'user', 'balance', 'get_created_at', 'get_created_at_jalali',
            'user_balance',
        )
        read_only_fields = (
            'id', 'user', 'get_created_at', 'get_created_at_jalali',
            'user_balance',
        )
