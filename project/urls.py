from django.urls import path, include
from project.views import ProjectView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'projects', ProjectView, basename='project')


urlpatterns = [
    path('', include(router.urls)),
]
