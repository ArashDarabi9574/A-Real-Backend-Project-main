from rest_framework import serializers

from page.models.model_page import Page


class PageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = (
            "id", 'title', 'content', 'slug', 'get_created_at_jalali', 'get_updated_at_jalali',
            'custom_template', 'meta_title', 'meta_description'
        )
        read_only_fields = (
            "id", 'title', 'content', 'slug', 'get_created_at_jalali', 'get_updated_at_jalali',
            'custom_template', 'meta_title', 'meta_description'
        )
