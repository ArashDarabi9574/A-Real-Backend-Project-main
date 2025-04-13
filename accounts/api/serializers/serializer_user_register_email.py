from django.core.validators import RegexValidator
from rest_framework import serializers


class UserRegisterEmailSerializer(serializers.Serializer):
    email_validator = RegexValidator(
        regex=r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', message="ایمیل درست نیست")
    email = serializers.CharField(max_length=256, validators=[email_validator])
