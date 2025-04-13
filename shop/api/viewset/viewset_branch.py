from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from shop.api.serializers import (
    BranchListSerializer,
    MainBranchSerializer
    )
from shop.models import Branch
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Branch"])
class BranchViewSet(viewsets.ModelViewSet):
    model = Branch
    serializer_class = MainBranchSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'delete', 'patch']
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'id']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
