from django.urls import include, path
from rest_framework.routers import DefaultRouter

from documents.views import DocumentView

router = DefaultRouter()
router.register(r"documents", DocumentView, basename="document")


urlpatterns = [
    path("", include(router.urls)),
]
