from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns_api_v1 = [
    path('', include('blog.urls_api'), name='main_blog'),
    path('', include('payment.urls_api'), name='main_payment'),
    path('', include('page.urls_api'), name='main_page'),
    path('', include('forms.urls_api'), name='main_forms'),
    path('', include('shop.urls_api'), name='main_shop'),
    path('', include('accounts.urls_api'), name='main_accounts'),
    path('', include('wallet.urls_api'), name='main_wallet'),
]

urlpatterns = [
    # urls admin
    path('admin/', admin.site.urls, name="admin_urls"),

    # urls drf_spectacular
    path('api/v1/schema/', SpectacularAPIView.as_view(api_version='v1'), name='schema'),
    path('api/v1/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # urls api
    path('api/v1/', include(urlpatterns_api_v1), name="api_urls"),

    # urls CkEditor
    path('ckeditor/', include('ckeditor_uploader.urls'), name="CKEditor_URL"),

]

# _______________________________ Static Config __________________________________________

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
