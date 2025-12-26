from django.urls import path
from timeline.views import TimelineView

# router = DefaultRouter()
# router.register(r'/register', UserView)
# router.register(r'/token', jwt_views.TokenObtainPairView.as_view(), basename='token')

urlpatterns = [
    path('timeline/', TimelineView.as_view()),
]
