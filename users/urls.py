from django.urls import path
from users.views import RegisterView, LoginView, LogoutView
from rest_framework_simplejwt import views as jwt_views

# router = DefaultRouter()
# router.register(r'/register', UserView)
# router.register(r'/token', jwt_views.TokenObtainPairView.as_view(), basename='token')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token'),
]
