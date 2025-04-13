from rest_framework import serializers

from page.models.model_page import Page


class PageCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = (
            'title', 'content', 'custom_template', 'meta_title', 'meta_description'
        )
