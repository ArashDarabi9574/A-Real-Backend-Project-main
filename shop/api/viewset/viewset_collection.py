from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from shop.api.serializers import (
    CollectionDetailSerializer,
    CollectionCreateUpdateSerializer,
    CollectionListSerializer
)
from shop.models import ProductsCollections
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response



@extend_schema(tags=["Collections"])
class CollectionViewSet(viewsets.ModelViewSet):
    model = ProductsCollections
    serializer_class = CollectionDetailSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'delete', 'patch']
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'slug']

    def get_queryset(self):
        if self.action == 'list' and not self.request.query_params.get('custom_list'):
            queryset = self.model.objects.filter(
                parent__isnull=True).order_by('position')
        else:
            queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list' and self.request.query_params.get('custom_list'):
            return CollectionDetailSerializer
        elif self.action == 'list':
            return CollectionListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return CollectionCreateUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()

