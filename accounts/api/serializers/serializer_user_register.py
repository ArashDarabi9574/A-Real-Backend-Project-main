from django.core.validators import RegexValidator
from rest_framework import serializers


class UserRegisterSerializer(serializers.Serializer):
    phone_number_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="The phone number is invalid.")
    phone_number = serializers.CharField(
        max_length=11, validators=[phone_number_validator])
