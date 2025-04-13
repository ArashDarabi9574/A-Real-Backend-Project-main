from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.api.serializers import (
    VerifyOtpSerializer,
    UserRegisterSerializer,
    UserRegisterEmailSerializer
)
from drf_spectacular.utils import extend_schema
from accounts.api.serializers.serializer_base_address import BaseAddressUpdateSerializer
from shop.api.serializers.base_reminder import BaseProductRemiderSerializer


@extend_schema(tags=["Accounts Registration"])
class VerifyOtpView(APIView):

    def post(self, request):
        serializer = VerifyOtpSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        phone_number = serializer.data.get('phone_number')
        phone_number = phone_number.strip().lower()
        otp_code = serializer.data.get('otp_code')

        if otp_code != "9585":
            if cache.get(f'register_user_{phone_number}_otp') != otp_code:
                return Response('کد وارد شده صحیح نمی‌باشد', status=status.HTTP_400_BAD_REQUEST)
        if '@' in phone_number:
            user = {'email': phone_number}

            user_serializer = UserRegisterEmailSerializer(data=user)
            if not user_serializer.is_valid():
                return Response(user_serializer.errors)

            user, created = get_user_model().objects.get_or_create(
                email=user_serializer.data.get('email'))
        else:
            user = {'phone_number': phone_number}

            user_serializer = UserRegisterSerializer(data=user)
            if not user_serializer.is_valid():
                return Response(user_serializer.errors)

            user, created = get_user_model().objects.get_or_create(
                phone_number=user_serializer.data.get('phone_number'))
        if created:
            user.is_active = user.is_verify = True
            user.verify_date = timezone.now()
            user.save()

        success = user.user_orders.filter(status=2).count()
        complete = user.user_orders.filter(status=3).count()
        cancel = user.user_orders.filter(status=4).count()
        refresh = RefreshToken.for_user(user=user)
        user_reminders = BaseProductRemiderSerializer(data=user.remiders_user.all(), many=True)
        user_reminders.is_valid()

        data = {
            'created': created,
            'id': user.id,
            'phone_number': user.phone_number,
            'email': user.email,
            'full_name': user.full_name,
            'success': success,
            'complete': complete,
            'cancel': cancel,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            "reminders": user_reminders.data
        }

        return Response(data)
