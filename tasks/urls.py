from django.urls import path
from tasks.views import TaskView, TaskViewDetail

# router = DefaultRouter()
# router.register(r'/register', UserView)
# router.register(r'/token', jwt_views.TokenObtainPairView.as_view(), basename='token')

urlpatterns = [
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:id>/', TaskViewDetail.as_view()),
]
