from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from timeline.models import Timeline
from timeline.serializer import TimelineSerializer


# Create your views here.
class TimelineView(APIView):
    serializer_class = TimelineSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Timeline.objects.all()
        serializer = TimelineSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
