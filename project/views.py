from rest_framework.viewsets import ModelViewSet
from project.models import Project
from project.serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class ProjectView(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
