from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, filters
from rest_framework import viewsets
from rest_framework.response import Response

from shop.api.serializers import (
    OrderItemListSerializer,
    OrderItemCreateUpdateSerializer
)
from shop.models import OrderItem
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Order Items"])
class OrderItemViewSet(viewsets.ModelViewSet):
    model = OrderItem
    serializer_class = OrderItemListSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'delete']
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['id',]

    def get_queryset(self):
        queryset = self.model.objects.select_related(
            'orders', 'products').all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderItemListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return OrderItemCreateUpdateSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
