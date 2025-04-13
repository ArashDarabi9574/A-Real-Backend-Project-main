from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('full_name', 'phone_number',
                  'email', 'national_number', 'permissions')

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get(
            'full_name', instance.full_name)
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.email = validated_data.get(
            'email', instance.email)
        instance.national_number = validated_data.get(
            'national_number', instance.national_number)
        instance.save()
        return instance
