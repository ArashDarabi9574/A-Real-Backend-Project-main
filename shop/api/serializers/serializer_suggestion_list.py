from rest_framework import serializers
from shop.models import Suggestion

from shop.api.serializers import BaseProductSerializer


class SuggestionListSerializer(serializers.ModelSerializer):
    primary_product = BaseProductSerializer(read_only=True)

    class Meta:
        model = Suggestion
        fields = ('id', 'primary_product', 'priority')
