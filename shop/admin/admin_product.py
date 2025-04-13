from django.contrib import admin
from model_clone import CloneModelAdmin


from shop.models import Product
from shop.admin.inline_suggestions import SuggestionInline
from shop.admin.inline_gallery import GalleryInline
from shop.admin.inline_attribute_style import ProductAttributeStyleInline
from shop.admin.inline_branch import BranchInline


@admin.register(Product)
class ProductAdmin(CloneModelAdmin):
    list_display = ('id', 'title', 'slug', 'main_price',
                    'brand',
                    'get_total_price',
                    'status', 'price_deadline',
                    )
    autocomplete_fields = ('set_watch', 'brand', )
    include_duplicate_action = True
    include_duplicate_object_link = True
    search_fields = (
        'id', 'title', 'brand__title', 'slug',
    )
    list_filter = ('brand', 'main_price',
                   'status', 'price_deadline', 'insurance')
    readonly_fields = ('created_at_jalali', 'updated_at_jalali',)
    ordering = ['-id', ]
    inlines = [ProductAttributeStyleInline,
               SuggestionInline, BranchInline, GalleryInline]

    fieldsets = (
        ('Main', {'fields': ('title', 'content', 'product_review', 'brand', 'collections', 'slug',
                             'set_watch', 'main_price', 'deadline_price', 'thumbnail', 'thumbnail_alt')}),
        ("Seo", {'fields': ("meta_title", 'meta_description')}),
        ("Setting", {'fields': ("status", 'special_tag',
                                'insurance')}),
        ("Date", {'fields': ('price_deadline',
                             "price_expired_date", )}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('title', 'content', 'product_review', 'brand', 'collections', 'slug',
                             'set_watch', 'main_price', 'deadline_price', 'thumbnail', 'thumbnail_alt')}),
        ("Seo", {'fields': ("meta_title", 'meta_description')}),
        ("Setting", {'fields': ("status", 'special_tag',
                                'insurance')}),
        ("Date", {'fields': ('price_deadline',
                             "price_expired_date", )}),
    )
