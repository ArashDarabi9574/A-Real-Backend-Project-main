from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from shop.api.serializers import (
    BrandDetailSerializer,
    BrandCreateUpdateSerializer,
    BrandListSerializer
)
from shop.models import Brand
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Brands"])
class BrandViewSet(viewsets.ModelViewSet):
    model = Brand
    serializer_class = BrandDetailSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'delete', 'patch']
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    pagination_class = None
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'country', 'slug']

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('position')
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return BrandListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return BrandCreateUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
