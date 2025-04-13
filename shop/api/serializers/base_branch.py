from rest_framework import serializers

from shop.models import ProductBranch


class BaseBranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductBranch
        fields = ('branch', 'inventory')
