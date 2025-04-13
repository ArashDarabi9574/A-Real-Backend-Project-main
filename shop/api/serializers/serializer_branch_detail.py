from rest_framework import serializers
from shop.models import ProductBranch


class BranchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBranch
        fields = ('id', 'branch', 'inventory')
        read_only_fields = ('id', 'branch', 'inventory')
