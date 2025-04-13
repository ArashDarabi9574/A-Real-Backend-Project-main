from rest_framework import serializers

from page.models.model_landing_page import LandingPage


class LandingPageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingPage
        fields = ('id', 'landing_page_name')
        read_only_fields = ('id', 'landing_page_name')
