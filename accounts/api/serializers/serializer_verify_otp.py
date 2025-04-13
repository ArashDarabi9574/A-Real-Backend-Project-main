from rest_framework import serializers


class VerifyOtpSerializer(serializers.Serializer):
    otp_code = serializers.CharField(max_length=4)
    phone_number = serializers.CharField(max_length=256)
