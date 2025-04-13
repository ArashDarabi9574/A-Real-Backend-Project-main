from django.urls import include, path
from rest_framework import routers
from blog.api.viewset.viewset_post import PostViewSet
from blog.api.viewset.viewset_category import CategoryViewSet
from blog.api.viewset.viewset_comment import PostCommentViewSet


router = routers.DefaultRouter()
router.register('post', PostViewSet, basename='post')
router.register('category', CategoryViewSet, basename='category')
router.register('comment', PostCommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls))
]
