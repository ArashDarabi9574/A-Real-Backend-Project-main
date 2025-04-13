from rest_framework import serializers

from shop.models import Product
from shop.api.serializers.base_gallery import BaseGallerySerializer


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title', 'content', 'product_review', 'meta_title', 'meta_description', 'main_price',
            'deadline_price', 'status', 'thumbnail_alt', 'price_deadline',
            'insurance', 'collections', 'brand', 'special_tag', 'set_watch', "images", "slug", "price_expired_date",
            "price_expired_date_jalali", "primary_suggestion", "images", "colors"
        )
