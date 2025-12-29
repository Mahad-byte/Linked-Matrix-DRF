from django.urls import include, path
from rest_framework.routers import DefaultRouter

from profiles.views import ProfileView

router = DefaultRouter()
router.register(r"profiles", ProfileView, basename="profile")


urlpatterns = [
    path("", include(router.urls)),
]
