from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from shop.api.serializers import (
    SpecialTagListSerializer,
    SpecialTagDetailSerializer,
    SpecialTagCreateUpdateSerializer
)
from shop.models import SpecialTag
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Special Tags"])
class SpecialTagViewSet(viewsets.ModelViewSet):
    model = SpecialTag
    serializer_class = SpecialTagDetailSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'delete', 'patch']
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', ]

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return SpecialTagListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return SpecialTagCreateUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
