from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from comments.views import CommentView, CommentDetailAPI

# router = DefaultRouter()
# router.register(r'/register', UserView)
# router.register(r'/token', jwt_views.TokenObtainPairView.as_view(), basename='token')

urlpatterns = [
    path('comments/', CommentView.as_view()),
    path('comments/<int:id>/', CommentDetailAPI.as_view()),
]
