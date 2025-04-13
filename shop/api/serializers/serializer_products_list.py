from rest_framework import serializers

from shop.models import Product
from shop.api.serializers.base_attributes import (
    BaseAttributeStyleSerializer
)
from utils.general.models.model_status_abstract import Choices


class ProductListSerializer(serializers.ModelSerializer):
    # special_tag = serializers.SlugRelatedField(
    #     many=True, read_only=True, slug_field='title')
    attribute_style = BaseAttributeStyleSerializer(
        many=True, read_only=True, source='product_tags')
    status = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'title', 'slug', 'thumbnail', 'status', 'special_tag',
            'main_price', 'deadline_price', 'get_total_price', 'get_price_expired_date',
            'get_discount_active', 'attribute_style', 'brand', 'collections'
        )

        read_only_fields = (
            'id', 'title', 'slug', 'thumbnail', 'status', 'special_tag',
            'main_price', 'deadline_price', 'get_total_price', 'get_price_expired_date',
            'get_discount_active', 'attribute_style', 'brand', 'collections'
        )
        depth = 1

    def get_status(self, obj):
        if obj.status == Choices.pre_order:
            return Choices.pre_order.label
        elif obj.status == Choices.out_stock:
            return Choices.out_stock.label
        else:
            stocks = obj.product_branch.values_list('inventory', flat=True)
            if stocks:
                try:
                    count = sum(stocks)
                    if count > 0:
                        return Choices.in_stock.label
                    else:
                        obj.status = Choices.out_stock.value
                        obj.save()
                        return Choices.out_stock.label
                except:
                    return Choices.out_stock.label
            else:
                return Choices.out_stock.label

class TorobProductSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='id')
    availability = serializers.SerializerMethodField()
    old_price = serializers.CharField(source='main_price')
    price = serializers.CharField(source='get_total_price')
    page_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'product_id', 'availability',
            'old_price', 'price',
            'page_url'
        )
        depth = 1

    def get_page_url(self, obj):
        return f"https://alizade-watchgallery.com/products/{obj.slug}"

    def get_availability(self, obj):
        if obj.status == Choices.pre_order:
            return Choices.pre_order.label
        elif obj.status == Choices.out_stock:
            return Choices.out_stock.label
        else:
            stocks = obj.product_branch.values_list('inventory', flat=True)
            if stocks:
                try:
                    count = sum(stocks)
                    if count > 0:
                        return Choices.in_stock.label
                    else:
                        obj.status = Choices.out_stock.value
                        obj.save()
                        return Choices.out_stock.label
                except:
                    return Choices.out_stock.label
            else:
                return Choices.out_stock.label

