# Core Django
from django.urls import path, include

app_name = 'forms'
urlpatterns = [
    path('', include('forms.api.router')),
]
