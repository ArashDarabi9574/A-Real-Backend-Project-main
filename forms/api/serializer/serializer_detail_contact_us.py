# 3rd Party
from rest_framework import serializers

# My App
from forms.models import ContactUs


class DetailContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id', 'name', 'email', 'phone_number', 'message', 'created_at', 'updated_at',
        )
