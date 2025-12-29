from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from profiles.models import Profile
from profiles.serializers import ProfileSerializer


# Create your views here.
class ProfileView(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
