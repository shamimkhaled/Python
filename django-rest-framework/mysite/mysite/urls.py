
from django.contrib import admin
from django.urls import include, path
from movies.views import MovieViewSet, ActionViewSet, ScifiViewSet
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

# Routers provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()
router = routers.SimpleRouter()
router.register('movies', MovieViewSet)
router.register('action', ActionViewSet)
router.register('scifi', ScifiViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include(router.urls)),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
