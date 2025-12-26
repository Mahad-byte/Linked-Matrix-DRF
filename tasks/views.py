from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from tasks.models import Task
from rest_framework.response import Response
from tasks.serializers import TaskSerializer
from rest_framework import status


# Create your views here.
class TaskView(APIView):
    serializer_class = TaskSerializer
    
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
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
        return Response(status=status.HTTP_204_NO_CONTENT)  
        
 