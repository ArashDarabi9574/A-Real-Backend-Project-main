from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from shop.api.serializers import (
    CommentListSerializer,
    CommentDetailSerializer,
    CommentCreateUpdateSerializer
)
from shop.models import Comment
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Product Comments"])
class CommentViewSet(viewsets.ModelViewSet):
    model = Comment
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    serializer_class = CommentDetailSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    http_method_names = ['get', 'post', 'delete', 'patch']
    search_fields = ['user__first_name', 'user__email',]
    filterset_fields = ['user__first_name', 'user__email', 'status', ]

    def get_queryset(self):
        queryset = self.model.objects.select_related('products').all()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CommentCreateUpdateSerializer
        elif self.action == 'list':
            return CommentListSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            return [permissions.IsAuthenticated()]
        elif self.action == 'destroy':
            return [permissions.IsAdminUser()]
        return super().get_permissions()
