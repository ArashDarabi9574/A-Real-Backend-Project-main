from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from shop.api.serializers import (
    SuggestionCreateUpdateSerializer,
    SuggestionDetailSerializer,
    SuggestionListSerializer
)
from shop.models import Suggestion
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Suggestions"])
class SuggestionViewSet(viewsets.ModelViewSet):
    model = Suggestion
    serializer_class = SuggestionDetailSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'delete', 'patch']
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['priority', ]

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return SuggestionListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return SuggestionCreateUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
