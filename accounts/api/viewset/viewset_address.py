from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from accounts.api.serializers import (
    AddressCreateUpdateSerializer,
    AddressDetailSerializer,
    AddressListSerializer
)
from accounts.models import UserAddress
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Address"])
class AddressViewSet(viewsets.ModelViewSet):
    model = UserAddress
    serializer_class = AddressDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'delete', 'patch']
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['postal_code',]

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return AddressListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return AddressCreateUpdateSerializer
        return self.serializer_class

    # def get_permissions(self):
    #     if self.action in ['create', 'update', 'partial_update', 'destroy']:
    #         return [permissions.IsAdminUser()]
    #     return super().get_permissions()
