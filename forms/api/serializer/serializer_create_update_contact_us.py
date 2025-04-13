# 3rd Party
from rest_framework import serializers

# My App
from forms.models import ContactUs


class CreateUpdateContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'name', 'email', 'phone_number', 'message'
        )
