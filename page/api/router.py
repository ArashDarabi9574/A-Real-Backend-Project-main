from rest_framework import routers
from page.api.viewset.viewset_page import PageViewSet
from page.api.viewset.viewset_landing_page import LandingPageViewSet


router = routers.DefaultRouter()
router.register('page', PageViewSet, basename='page')
router.register('landing_page', LandingPageViewSet, basename='landing_page')
urlpatterns = router.urls
