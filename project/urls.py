from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from project.views import ProjectView, ProjectDetailAPI

# router = DefaultRouter()
# router.register(r'/register', UserView)
# router.register(r'/token', jwt_views.TokenObtainPairView.as_view(), basename='token')

urlpatterns = [
    path('projects/', ProjectView.as_view()),
    path('projects/<int:id>/', ProjectDetailAPI.as_view()),
]
