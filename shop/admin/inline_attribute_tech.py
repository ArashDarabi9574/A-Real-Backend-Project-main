from django.contrib import admin

from shop.models.model_product_attribute_tech import ProductAttributeTech


class ProductAttributeTechInline(admin.TabularInline):
    model = ProductAttributeTech
    extra = 8

    fieldsets = (
        ('Main', {'fields': ('products_tag', 'content', 'position')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('products_tag', 'content', 'position')}),
    )
