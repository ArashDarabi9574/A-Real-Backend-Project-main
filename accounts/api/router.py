from django.urls import include, path
from rest_framework import routers
from accounts.api import viewset

router = routers.DefaultRouter()
router.register('users', viewset.UserViewSet, basename='users')
router.register('address', viewset.AddressViewSet, basename='address'),

urlpatterns = [
    path('register/', viewset.RegisterUserView.as_view(), name='register'),
    path('verify-otp/', viewset.VerifyOtpView.as_view(), name='verify_otp'),
    path('', include(router.urls)),
]
