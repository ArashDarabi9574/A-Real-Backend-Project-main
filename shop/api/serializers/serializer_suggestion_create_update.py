from rest_framework import serializers
from shop.models import Suggestion


class SuggestionCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Suggestion
        fields = ('primary_product', 'suggestions', 'priority')
