from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from tasks.models import Task
from project.models import Project
from profiles.models import Profile
from rest_framework.response import Response
from tasks.serializers import TaskSerializer
from rest_framework import status


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
    
    
class TaskViewDetail(APIView):
    serializer_class = TaskSerializer
    
    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, id):
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
        
    def delete(self, request, id):
        task = get_object_or_404(Task, id=id)
        task.delete()
        return Response("Deleted!!", status=status.HTTP_400_BAD_REQUEST)  
        
 