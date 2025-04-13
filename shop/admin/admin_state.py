from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from shop.models import State


class StateResource(resources.ModelResource):
    class Meta:
        model = State
        fields = ("id", 'name', 'slug')
        export_order = ("id", 'name', 'slug')


@admin.register(State)
class StateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('-id',)
    resource_class = StateResource

    fieldsets = (('Main', {'fields': ('name', 'slug')}),)
    add_fieldsets = (('Main', {'fields': ('name', 'slug')}),)
