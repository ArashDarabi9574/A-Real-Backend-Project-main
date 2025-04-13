from django.contrib import admin

from shop.models.model_product_attribute_style import ProductAttributeStyle


class ProductAttributeStyleInline(admin.TabularInline):
    model = ProductAttributeStyle
    extra = 8

    fieldsets = (
        ('Main', {'fields': ('products_tag', 'content', 'position')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('products_tag', 'content', 'position')}),
    )
