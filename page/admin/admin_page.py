from django.contrib import admin
from page.models.model_page import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'custom_template', 'slug',
                    'get_created_at_jalali', 'get_updated_at_jalali')
    search_fields = ('title', 'slug')

    fieldsets = (
        ('Main', {'fields': ('title', 'slug',
                             'content', 'custom_template')}),
        ("Seo information", {'fields': ("meta_title", "meta_description")}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('title', 'slug',
         'content', 'custom_template')}),
        ("Seo information", {'fields': ("meta_title", "meta_description")}),
    )
