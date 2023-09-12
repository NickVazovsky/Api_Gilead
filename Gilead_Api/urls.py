from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title='Gilead API docs',
        default_version='v1',
        description='This documentation is created to help Maxim',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='nvazovsky@gmail.com'),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/video/', include('test_video.urls')),
    path('api/news/', include('news.urls')),
    path('api/materials/', include('material_app.urls')),
    path('api/instructions/', include('instructions.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
