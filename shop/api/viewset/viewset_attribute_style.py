from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from shop.api.serializers import (
    ProductAttributeStyleCreateUpdateSerializer,
    AttributeStyleDetailSerializer,
    AttributeStyleListSerializer,

)
from shop.api.serializers.serializer_attributes_detail import AttributeStyleSerializer

from shop.models import ProductAttributeStyle, AttributeStyle
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Attribute Style"])
class AttributeStyleViewSet(viewsets.ModelViewSet):
    model = ProductAttributeStyle
    serializer_class = AttributeStyleDetailSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'delete', 'patch']
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'id']

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('position')
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return AttributeStyleListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return ProductAttributeStyleCreateUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()


@extend_schema(tags=["Attribute Style"])
class AttributeStyleListViewSet(viewsets.ModelViewSet):
    model = AttributeStyle
    serializer_class = AttributeStyleSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'delete']
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'id']

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('position')
        return queryset

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
