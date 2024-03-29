
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


# Create a schema view for Assets API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Product Document Management API Documentation",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    # For Swagger UI URL
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/', include('docu_upload.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
