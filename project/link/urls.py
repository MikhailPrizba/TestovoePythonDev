from django.urls import include, path
from rest_framework import routers
from .views import LinkViewSet

router = routers.DefaultRouter()
router.register(r"", LinkViewSet, basename="link")

urlpatterns = [
    path("", include(router.urls)),
]