from rest_framework import serializers
from shop.models import Suggestion

from shop.api.serializers import BaseProductSerializer
from shop.api.serializers.base_suggestions import BaseSuggestionsSerializer


class SuggestionDetailSerializer(serializers.ModelSerializer):
    primary_product = BaseProductSerializer(read_only=True)
    suggestions = BaseSuggestionsSerializer(read_only=True)

    class Meta:
        model = Suggestion
        fields = ('id', 'primary_product', 'suggestions', 'priority')
