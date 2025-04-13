from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions

from django_filters.rest_framework import DjangoFilterBackend

from page.models.model_page import Page
from page.api.serializer.serializer_page_list import PageListSerializer
from page.api.serializer.serializer_page_create_update import PageCreateUpdateSerializer
from page.api.serializer.serializer_page_detail import PageDetailSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Pages"])
class PageViewSet(viewsets.ModelViewSet):
    model = Page
    serializer_class = PageDetailSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    http_method_names = ['get', 'post', 'delete']
    search_fields = ['title', 'slug', ]
    filterset_fields = ['title', 'slug', ]
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return PageListSerializer
        if self.action in ['create', 'update', 'partial_update']:
            return PageCreateUpdateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
