from rest_framework import serializers

from shop.models import Gallery


class BaseGallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ('image', 'image_alt')
