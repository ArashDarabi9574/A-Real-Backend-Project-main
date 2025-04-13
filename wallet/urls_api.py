from django.urls import path, include

app_name = 'wallet'
urlpatterns = [
    path('wallet/', include('wallet.api.router')),
]
