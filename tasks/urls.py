from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tasks.views import TaskView

router = DefaultRouter()
router.register(r"tasks", TaskView, basename="task")


urlpatterns = [
    path("", include(router.urls)),
]
