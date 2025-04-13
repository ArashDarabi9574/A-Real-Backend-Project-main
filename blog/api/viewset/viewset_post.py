from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend

from blog.models.model_blog_post import Post

from blog.api.serializers.serializer_list_post import ListPostSerializer
from blog.api.serializers.serializer_detail_post import DetailPostSerializer
from blog.api.serializers.serializer_create_update_post import CreateUpdatePostSerializer
from drf_spectacular.utils import extend_schema
from core.pagination import CustomPagination


@extend_schema(tags=["Posts"])
class PostViewSet(viewsets.ModelViewSet):
    model = Post
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    http_method_names = ['get', 'post', 'delete', 'patch']
    serializer_class = DetailPostSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    pagination_class = CustomPagination
    search_fields = ['title', 'slug', 'author__phone_number',
                     'category__title',]
    ordering_fields = ('created_at', )
    ordering = ('-created_at', )
    filterset_fields = ['title', 'slug',
                        'category__title', 'author__phone_number', 'status']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ListPostSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return CreateUpdatePostSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
