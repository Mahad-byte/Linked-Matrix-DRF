from django.urls import path
from tasks.views import TaskView

# router = DefaultRouter()
# router.register(r'/register', UserView)
# router.register(r'/token', jwt_views.TokenObtainPairView.as_view(), basename='token')

urlpatterns = [
    path('tasks/', TaskView.as_view()),
    # path('projects/<int:id>/', ProjectDetailAPI.as_view()),
]
