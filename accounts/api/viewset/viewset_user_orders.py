from rest_framework import permissions
from rest_framework import viewsets

from shop.api.serializers import (
    OrderListSerializer,
    OrderCreateUpdateSerializer,
    OrderDetailSerializer
)
from shop.models import Order
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["User Orders"])
class UserOrderViewSet(viewsets.ModelViewSet):
    model = Order
    serializer_class = OrderDetailSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user)
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
            return [permissions.IsAuthenticated()]
        return super().get_permissions()
