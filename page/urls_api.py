from django.urls import path, include

app_name = 'page'
urlpatterns = [
    path('', include('page.api.router'))
]
