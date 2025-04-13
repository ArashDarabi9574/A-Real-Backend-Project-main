from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from shop.api.serializers import (
    ColorListSerializer,
    ColorDetailSerializer,
    ColorCreateUpdateSerializer
)
from shop.models import Colors
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Color"])
class ColorViewSet(viewsets.ModelViewSet):
    model = Colors
    serializer_class = ColorDetailSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'delete']
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['color_name', 'id']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ColorListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return ColorCreateUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
