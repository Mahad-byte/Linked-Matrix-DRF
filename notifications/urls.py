from django.urls import path
from notifications.views import NotificationView

# router = DefaultRouter()
# router.register(r'/register', UserView)
# router.register(r'/token', jwt_views.TokenObtainPairView.as_view(), basename='token')

urlpatterns = [
    path('notifications/', NotificationView.as_view()),
    path('notifications/<int:id>/mark_read/', NotificationView.as_view()),
]
