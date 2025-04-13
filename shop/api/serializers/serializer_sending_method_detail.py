from rest_framework import serializers
from shop.models import SendingMethod


class SendingMethodDetailSerializer(serializers.ModelSerializer):
    states = serializers.CharField(source="get_state_list")

    class Meta:
        model = SendingMethod
        fields = ('id', 'title', 'price', 'free_price', 'status', 'description', "states")
