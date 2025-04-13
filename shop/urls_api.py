from django.urls import path, include

app_name = 'shop'
urlpatterns = [
    path('shop/', include('shop.api.router')),
]
