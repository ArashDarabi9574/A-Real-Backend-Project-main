from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': 'نام‌کاربری یا رمزعبور اشتباه است.'
    }

    def validate(self, attrs):
        validated_data = super().validate(attrs)

        if not self.user:
            raise serializers.ValidationError(
                'نام‌کاربری یا رمزعبور اشتباه است')

        validated_data['user_id'] = self.user.id
        validated_data['username'] = self.user.username
        validated_data['email'] = self.user.email
        validated_data['full_name'] = self.user.full_name
        validated_data['phone_number'] = self.user.phone_number
        validated_data['national_number'] = self.user.national_number
        validated_data['super_user'] = self.user.is_superuser
        try:
            permissions = [key for key, value in vars(self.user.permissions).items() if value]
        except:
            permissions = None
        validated_data['permissions'] = permissions

        return validated_data
