from rest_framework import serializers

from page.models.model_sliders import (
    Slider,
    Icons,
    UnderSlider
)


class BaseSliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = ('slider_link', 'slider_image', 'slider_image_alt')


class BaseIconSerializer(serializers.ModelSerializer):

    class Meta:
        model = Icons
        fields = ('icon_name', 'icon_link',
                  'icon_thumbnail', 'icon_thumbnail_alt')


class BaseUnderSliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnderSlider
        fields = ('under_slider_image', 'under_slider_image_alt', 'under_slider_link')
