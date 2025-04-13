from rest_framework import serializers

from page.models.model_landing_page import LandingPage
from page.api.serializer.Base_slider_icon import (
    BaseSliderSerializer,
    BaseIconSerializer,
    BaseUnderSliderSerializer
)
from page.api.serializer.serializer_base_menu import *


class LandingPageDetailSerializer(serializers.ModelSerializer):
    landing_slider = BaseSliderSerializer(
        many=True, source='sliders')
    landing_under_slider = BaseUnderSliderSerializer(
        many=True, source='under_slider')
    landing_icons = BaseIconSerializer(
        many=True, source='icons')
    landing_up_menu = UpMenuSerializer(many=True, source='up_menu')
    landing_down_right_menu = DownRightMenuSerializer(many=True, source='down_right_menu')
    landing_down_middle_menu = DownLeftMenuerializer(many=True, source='down_middle_menu')
    landing_down_left_menu = DownMiddleMenuSerializer(many=True, source='down_left_menu')

    class Meta:
        model = LandingPage
        depth = 1
        fields = ('id', 'landing_page_name', 'button_image',
                  'button_image_alt', 'button_link',
                  'landing_slider', 'landing_under_slider', 'landing_icons',
                  'special_link_1', 'special_image_1', 'special_title_1', 'special_desc_1',
                    'special_link_2', 'special_image_2', 'special_title_2', 'special_desc_2',
                    'special_link_3', 'special_image_3', 'special_title_3', 'special_desc_3',
                    'quick_access_name', 'quick_access_link',
                    'landing_up_menu', 'landing_down_right_menu', 'landing_down_middle_menu', 'landing_down_left_menu')

        read_only_fields = ('id', 'landing_page_name', 'button_image',
                            'button_image_alt', 'button_link',
                            'landing_slider', 'landing_under_slider', 'landing_icons',
                            'special_link_1', 'special_image_1', 'special_title_1', 'special_desc_1',
                    'special_link_2', 'special_image_2', 'special_title_2', 'special_desc_2',
                    'special_link_3', 'special_image_3', 'special_title_3', 'special_desc_3',
                    'quick_access_name', 'quick_access_link',
                    'landing_up_menu', 'landing_down_right_menu', 'landing_down_middle_menu', 'landing_down_left_menu')
