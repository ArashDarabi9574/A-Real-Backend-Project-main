from rest_framework import routers
from forms.api import viewset

router = routers.DefaultRouter()
router.register('contact-us', viewset.ContactUsViewSet, basename='contact_us')

urlpatterns = router.urls
