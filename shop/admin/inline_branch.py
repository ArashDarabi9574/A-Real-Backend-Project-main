from django.contrib import admin

from shop.models.model_product_branch import ProductBranch


class BranchInline(admin.TabularInline):
    model = ProductBranch

    fieldsets = (
        ('Main', {'fields': ('branches', 'inventory',)}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('branches', 'inventory',)}),
    )
