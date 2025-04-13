# 3rd Party
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

# My App
from blog.models import PostComment
from blog.api.serializers.serializer_create_update_comment import CreateUpdateCommentSerializer
from blog.api.serializers.serializer_list_comment import ListCommentSerializer
from blog.api.serializers.serializer_detail_comment import DetailCommentSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Post Comments"])
class PostCommentViewSet(viewsets.ModelViewSet):
    model = PostComment
    lookup_field = 'pk'
    http_method_names = ['get', 'post', 'delete', 'patch']
    serializer_class = DetailCommentSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['user__first_name', 'user__email', 'post__title',
                     'post__slug',]
    filterset_fields = ['user__first_name', 'user__email', 'post__title',
                        'post__slug', 'rate']
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreateUpdateCommentSerializer
        elif self.action == 'list':
            return ListCommentSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            return [permissions.IsAuthenticated()]
        elif self.action == 'destroy':
            return [permissions.IsAdminUser]
        return super().get_permissions()
