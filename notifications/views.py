from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from notifications.serializer import NotificationSerializer
from notifications.models import Notification


# Create your views here.
class NotificationView(APIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id is not None:
            notification = Notification.objects.get(id=id)
            notification.mark_read = True
            notification.save()
        queryset = Notification.objects.all()
        serializer = NotificationSerializer(queryset, many=True)
        return Response(serializer.data)
