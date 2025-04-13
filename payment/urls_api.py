from django.urls import path

from . import views

app_name = 'payment'
urlpatterns = [
    path('payment/request/zarrinpal/<int:order_id>/',
         views.send_request, name='send_request'),
    path('payment/verify/zarrinpal/<int:order_id>/', views.verify, name='verify'),
]
