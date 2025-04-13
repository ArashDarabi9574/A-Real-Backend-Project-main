from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from shop.api.serializers import (
    BaseProductRemiderSerializer,
    CreateProductRemiderSerializer
)
from shop.models import ProductRemider
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Reminder"])
class ReminderView(viewsets.ModelViewSet):
    model = ProductRemider
    serializer_class = BaseProductRemiderSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'delete']
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreateProductRemiderSerializer
        return self.serializer_class

    # def get_permissions(self):
    #     if self.action in ['create', 'update', 'destroy']:
    #         return [permissions.IsAdminUser()]
    #     return super().get_permissions()
