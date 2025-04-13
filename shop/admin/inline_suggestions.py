from django.contrib import admin

from shop.models import Suggestion


class SuggestionInline(admin.TabularInline):
    model = Suggestion
    extra = 5
    fk_name = 'primary_product'
    autocomplete_fields = ('suggestions',)
