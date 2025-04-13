from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from shop.api.serializers import (
    SendingMethodDetailSerializer,
    SendingMethodCreateUpdateSerializer,
    SendingMethodListSerializer
)
from shop.models import SendingMethod
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Sending Method"])
class SendingMethodViewSet(viewsets.ModelViewSet):
    model = SendingMethod
    serializer_class = SendingMethodDetailSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'state__title', 'state__slug']

    def get_queryset(self):
        queryset = self.model.objects.prefetch_related('state').all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return SendingMethodListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return SendingMethodCreateUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
