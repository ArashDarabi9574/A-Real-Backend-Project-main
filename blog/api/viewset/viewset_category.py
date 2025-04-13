from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions

from blog.models.model_blog_post_category import PostCategory
from blog.api.serializers.serializer_list_category import ListCategorySerializer
from blog.api.serializers.serializer_create_update_category import CreateUpdateCategorySerializer
from blog.api.serializers.serializer_detail_category import DetailCategorySerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Categories"])
class CategoryViewSet(viewsets.ModelViewSet):
    model = PostCategory
    lookup_field = 'pk'
    permission_classes = [permissions.AllowAny]
    serializer_class = DetailCategorySerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['id', 'title',]
    filterset_fields = ['title',]
    http_method_names = ['get', 'post', 'delete', 'patch']

    def get_queryset(self):
        queryset = PostCategory.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ListCategorySerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return CreateUpdateCategorySerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
