from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from shop.api.serializers import (
    DiscountListSerializer,
    DiscountDetailSerializer,
    DiscountCreateUpdateSerializer
)
from shop.models import Discount
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Discounts"])
class DiscountViewSet(viewsets.ModelViewSet):
    model = Discount
    serializer_class = DiscountDetailSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'delete']
    lookup_field = 'code'
    lookup_url_kwarg = 'code'

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['code', 'title', 'percentage',]
    filterset_fields = ['type_discount']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return DiscountListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return DiscountCreateUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
