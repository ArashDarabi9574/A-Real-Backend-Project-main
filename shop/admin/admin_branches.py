from django.contrib import admin
from shop.models import Branch


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    ordering = ['-id', ]
    search_fields = (
        'id', 'title',
    )
    fieldsets = (
        ('Main', {'fields': ('title',)}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('title',)}),
    )
