from rest_framework import serializers

from page.models.model_page import Page


class PageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = fields = (
            "id", 'title', 'slug', 'get_created_at_jalali', 'custom_template',
        )
        read_only_fields = (
            "id", 'title', 'slug', 'get_created_at_jalali', 'custom_template',
        )
