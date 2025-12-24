from django.shortcuts import render
from rest_framework.views import APIView
from project.models import Project
from project.serializers import ProjectSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


# Create your views here.
class ProjectView(APIView):
    serializer_class = ProjectSerializer

    def post(self, request):
        new_project = Project.objects.create(
            title="DRF Training", # TODO
            description="Backend API development"
        )
        new_project.save()
        return Response(f"Added the project with id {new_project}")

    def get(self, request):
        queryset = Project.objects.all()
        return Response(f"Retruning Projects: {queryset}")
    

class ProjectDetailAPI(APIView):
    serializer_class = ProjectSerializer

    def get(self, request, id):
        project = get_object_or_404(Project, id=id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, id):
        project = get_object_or_404(Project, id=id)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    def delete(self, request, id):
        project = get_object_or_404(Project, id=id)
        project.delete()
        return Response("Deleted!!", status=status.HTTP_400_BAD_REQUEST)  
          