from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from accounts.api.serializers import (
    UserUpdateSerializer,
    UserDetailSerializer,
    UserListSerializer
)
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Users"])
class UserViewSet(viewsets.ModelViewSet):
    model = get_user_model()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'delete', 'patch']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_staff', 'permissions__name']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        elif self.action in ['update', 'partial_update', 'patch']:
            return UserUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.IsAdminUser()]
        return super().get_permissions()
