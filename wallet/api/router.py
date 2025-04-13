from django.urls import include, path
from rest_framework import routers
from wallet.api.viewset import (
    WalletViewset,
    TransactionViewset
)

router = routers.DefaultRouter()
router.register('wallet', WalletViewset, basename='wallet')
router.register('transaction', TransactionViewset, basename='transaction')

urlpatterns = [
    path('', include(router.urls))
]
