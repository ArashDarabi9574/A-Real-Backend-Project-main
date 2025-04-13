from rest_framework import viewsets, permissions, filters

from wallet.models import Wallet
from django_filters.rest_framework import DjangoFilterBackend
from wallet.api.serializers import (
    TransactionCreateUpdateSerializer,
    TransactionDetailSerializer,
    TransactionListSerializer
)
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Wallet Transactions"])
class TransactionViewset(viewsets.ModelViewSet):
    model = Wallet
    serializer_class = TransactionDetailSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'delete',]
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['id',]

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return TransactionListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return TransactionCreateUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
