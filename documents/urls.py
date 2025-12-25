from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from documents.views import DocumentView, DocumentDetailAPI

# router = DefaultRouter()
# router.register(r'/register', UserView)
# router.register(r'/token', jwt_views.TokenObtainPairView.as_view(), basename='token')

urlpatterns = [
    path('documents/', DocumentView.as_view()),
    path('documents/<int:id>/', DocumentDetailAPI.as_view()),
]
