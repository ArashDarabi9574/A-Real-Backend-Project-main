from rest_framework import serializers

from shop.models import OrderItem
from shop.api.serializers.base_products import BaseProductSerializer


class OrderItemForInvoiceSerializer(serializers.ModelSerializer):
    discount_amount = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    main_price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ("products", "quantity", "main_price", "discount_amount", "total_price")

    def get_main_price(self, obj):
        return obj.products.main_price

    def get_discount_amount(self, obj):
        by_seller = obj.products.deadline_price
        return by_seller

    def get_products(self, obj):
        product = BaseProductSerializer(obj.products).data
        return product['title']

    def get_total_price(self, obj):
        discount = self.get_discount_amount(obj=obj)
        if discount is not None:
            final_price = (obj.products.main_price - discount) * obj.quantity
        else:
            final_price = (obj.products.main_price) * obj.quantity
        return final_price
