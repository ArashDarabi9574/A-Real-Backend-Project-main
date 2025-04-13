from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions

from django_filters.rest_framework import DjangoFilterBackend

from page.models.model_landing_page import LandingPage
from page.api.serializer.serializer_landing_list import LandingPageListSerializer
from page.api.serializer.serializer_landing_create_update import LandingPageCreateUpdateSerializer
from page.api.serializer.serializer_landing_detail import LandingPageDetailSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Landing Page"])
class LandingPageViewSet(viewsets.ModelViewSet):
    model = LandingPage
    serializer_class = LandingPageDetailSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    http_method_names = ['get', 'post', 'delete']
    search_fields = ['id', 'landing_page_name']
    filterset_fields = ['id', ]

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return LandingPageListSerializer
        if self.action in ['create', 'update', 'partial_update']:
            return LandingPageCreateUpdateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
