from rest_framework import serializers
from shop.models import Branch, ProductBranch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('title',)

class MainBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('id', 'title',)

class ProductBranchCreateUpdateSerializer(serializers.ModelSerializer):

    branches = BranchSerializer()

    class Meta:
        model = ProductBranch
        fields = ('branches',)

    def create(self, validated_data):
        branches_data = validated_data.pop('branches')
        branches = Branch.objects.create(**branches_data)
        return ProductBranch.objects.create(branches=branches, **validated_data)
