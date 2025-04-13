from rest_framework import serializers

from shop.models import Suggestion


class BaseSuggestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        depth = 1
        fields = ('suggestions', 'priority')
