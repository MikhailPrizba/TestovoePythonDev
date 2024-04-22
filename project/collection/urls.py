from django.urls import include, path
from rest_framework import routers
from .views import CollectionViewSet

router = routers.DefaultRouter()
router.register(r"", CollectionViewSet, basename="collection")

urlpatterns = [
    path("", include(router.urls)),
]
