from rest_framework import serializers

from shop.models import Product
from shop.api.serializers.base_brand import BaseBrandSerializer

from shop.api.serializers.base_suggestions import BaseSuggestionsSerializer
from shop.api.serializers.base_branch import BaseBranchSerializer
from shop.api.serializers.base_attributes import (
    BaseAttributeStyleSerializer,
    BaseAttributeTechSerializer
)
from shop.api.serializers.base_gallery import BaseGallerySerializer
from shop.models.model_comment import Comment
from shop.api.serializers.base_comments import BaseProductCommentSerializer
from shop.api.serializers.base_set_watch import SetWatchSerializer
from shop.api.serializers.base_collection import BaseCollectionSerializer
from utils.general.models.model_status_abstract import Choices


class ProductDetailSerializer(serializers.ModelSerializer):
    brand = BaseBrandSerializer(read_only=True)
    collections = BaseCollectionSerializer(
        many=True, read_only=True)
    # special_tag = serializers.SlugRelatedField(
    #     many=True, read_only=True, slug_field='title')
    branch = BaseBranchSerializer(many=True, source='product_branch')
    attribute_style = BaseAttributeStyleSerializer(
        many=True, source='product_tags')
    attribute_tech = BaseAttributeTechSerializer(
        many=True, source='product_tech_attr')
    gallery = BaseGallerySerializer(
        many=True, source='images')
    comments = serializers.SerializerMethodField()
    set_watch = SetWatchSerializer(read_only=True)
    status = serializers.SerializerMethodField()

    class Meta:
        model = Product
        depth = 1
        fields = (
            'id', 'title', 'meta_title', 'content', 'meta_description', 'product_review', 'thumbnail', 'thumbnail_alt', 'set_watch', 'status',
            'special_tag', 'main_price', 'deadline_price', 'branch', 'attribute_style', 'gallery',
            'attribute_tech', 'price_deadline', 'collections', 'suggestions',
            'brand', 'insurance', 'get_price_expired_date', 'comments',
            'get_total_price', 'slug', 'get_created_at_jalali', 'get_updated_at_jalali', 'get_discount_active'
        )

        read_only_fields = (
            'id', 'title', 'meta_title', 'content', 'meta_description', 'product_review', 'thumbnail', 'thumbnail_alt', 'set_watch', 'status',
            'special_tag', 'main_price', 'deadline_price', 'branch', 'attribute_style', 'gallery',
            'attribute_tech', 'price_deadline', 'collections', 'suggestions',
            'brand', 'insurance', 'get_price_expired_date', 'comments',
            'get_total_price', 'slug', 'get_created_at_jalali', 'get_updated_at_jalali', 'get_discount_active'
        )

    def get_comments(self, obj):
        top_level_comments = Comment.objects.filter(
            products=obj, status=Comment.Choices.publish.value)
        if top_level_comments:
            return BaseProductCommentSerializer(top_level_comments, many=True, read_only=True).data
        return []

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
                    obj.status = Choices.out_stock.value
                    obj.save()
                    return Choices.out_stock.label
            else:
                obj.status = Choices.out_stock.value
                obj.save()
                return Choices.out_stock.label
