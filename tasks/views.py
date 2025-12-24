from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from tasks.models import Task
from project.models import Project
from profiles.models import Profile
from rest_framework.response import Response
from tasks.serializers import TaskSerializer


# Create your views here.
class TaskView(APIView):
    serializer_class = TaskSerializer
    
    def get(self, request):
        tasks = Task.objects.all()
        return Response(f"Tasks: {tasks}")
    
    def post(self, request):
        title = request.data.get('title')
        Description = request.data.get('description')
        status = request.data.get('status')
        project_id = request.data.get('project')
        asignee_id = request.data.get('asignee')
        project_instance = get_object_or_404(Project, id=project_id)
        asignee_instance = get_object_or_404(Profile, id=asignee_id)

        task = Task.objects.create(title=title, description=Description, status=status, 
                                   project=project_instance, asignee=asignee_instance)
        task.save()
        return Response("Saved!")