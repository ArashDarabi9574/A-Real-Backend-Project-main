from django.urls import path, include

from accounts.api.viewset import (
    CustomTokenObtainPairViewSet,
    CustomTokenRefreshView
)

app_name = 'accounts'
urlpatterns = [
    path('accounts/', include('accounts.api.router')),
    path('accounts/token/', CustomTokenObtainPairViewSet.as_view(),
         name='token_obtain_pair'),
    path('accounts/token/refresh/',
         CustomTokenRefreshView.as_view(), name='token_refresh'),
]
