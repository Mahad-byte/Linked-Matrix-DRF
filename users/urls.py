from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from users.views import LogoutView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # path('logout/', jwt_views.TokenBlacklistView.as_view(), name='logout'),
    path("login/", jwt_views.TokenObtainPairView.as_view(), name="login"),
]
