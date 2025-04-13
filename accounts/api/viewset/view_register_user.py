from django.core.cache import cache
from django.core.mail import EmailMessage
from django.template.loader import get_template
from utils.generator import generate_code

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.api.serializers import (
    UserRegisterSerializer,
    UserRegisterEmailSerializer
)
from utils.sender import sms_sender
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Accounts Registration"])
class RegisterUserView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number', None)
        if phone_number is None:
            return Response({"error": 'It is necessary to send a phone number'}, status=status.HTTP_400_BAD_REQUEST)

        # code = '1234'
        code = generate_code(length=4, number=True, character=False)
        if '@' in phone_number:
            validate_email = UserRegisterEmailSerializer(
                data={'email': phone_number})
            if not validate_email.is_valid():
                return Response(validate_email.errors, status=status.HTTP_400_BAD_REQUEST)
            if cache.get(f'register_user_{phone_number}_otp') is not None:
                return Response('کد ارسال شده است .', status=status.HTTP_200_OK)

            data = {
                "code": code,
            }

            email_message = get_template('register_email.html').render(data)

            try:
                msg = EmailMessage(
                    f"کد ورود شما به سایت",
                    email_message,
                    'گالری ساعت علیزاده <noreply@alizadeh-watchgallery.com>',
                    [phone_number]
                )
                msg.content_subtype = "html"
                msg.send()

            except:
                pass
        else:
            validated_phone_number = UserRegisterSerializer(
                data={'phone_number': phone_number})
            if not validated_phone_number.is_valid():
                return Response(validated_phone_number.errors, status=status.HTTP_400_BAD_REQUEST)

            if cache.get(f'register_user_{phone_number}_otp') is not None:
                return Response('کد قبلاً ارسال شده است', status=status.HTTP_200_OK)

            # Send SMS
            sms_sender(number=phone_number, usage="user_register", code=code)

        # add code in redis
        cache.set(f'register_user_{phone_number}_otp', code, 120)

        # add user temporarily
        cache.set(f'temp_user_{phone_number}', phone_number, 120)

        return Response('کد ارسال شده است', status=status.HTTP_200_OK)
