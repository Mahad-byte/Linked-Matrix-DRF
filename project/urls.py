from django.urls import path, include
from rest_framework.routers import DefaultRouter

from project.views import ProjectView


router = DefaultRouter()
router.register(r"projects", ProjectView, basename="project")


urlpatterns = [
    path("", include(router.urls)),
]
