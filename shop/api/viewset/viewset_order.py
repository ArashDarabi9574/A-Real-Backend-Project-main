from rest_framework import permissions
from rest_framework import viewsets

from shop.api.serializers import (
    OrderListSerializer,
    OrderCreateUpdateSerializer,
    OrderDetailSerializer
)
from shop.models import Order
from drf_spectacular.utils import extend_schema
from core.pagination import CustomPagination2


@extend_schema(tags=["Orders"])
class OrderViewSet(viewsets.ModelViewSet):
    model = Order
    serializer_class = OrderDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post', 'delete', 'patch']
    pagination_class = CustomPagination2

    def get_queryset(self):
        queryset = self.model.objects.select_related('user').all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return OrderCreateUpdateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
