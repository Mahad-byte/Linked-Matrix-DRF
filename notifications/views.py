from django.shortcuts import render
from rest_framework.views import APIView
from notifications.serializer import NotificationSerializer
from notifications.models import Notification
from rest_framework.response import Response

# Create your views here.
class NotificationView(APIView):
    serializer_class = NotificationSerializer
    
    def get(self, request, id=None):
        if id is not None:
            notification = Notification.objects.get(id=id)
            notification.mark_read = True
            notification.save()
        queryset = Notification.objects.all()
        serializer = NotificationSerializer(queryset, many=True)
        return Response(serializer.data)