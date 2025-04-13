from rest_framework import serializers

from page.models.model_landing_page import LandingPage
from page.api.serializer.Base_slider_icon import (
    BaseSliderSerializer,
    BaseIconSerializer,
    BaseUnderSliderSerializer
)


class LandingPageCreateUpdateSerializer(serializers.ModelSerializer):
    landing_slider = BaseSliderSerializer()
    landing_under_slider = BaseUnderSliderSerializer()
    landing_icons = BaseIconSerializer()

    class Meta:
        model = LandingPage
        fields = ('landing_page_name', 'button_image',
                  'button_image_alt', 'landing_slider', 'landing_under_slider', 'landing_icons')
