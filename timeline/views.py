from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from timeline.models import Timeline
from timeline.serializer import TimelineSerializer


# Create your views here.
class TimelineView(ListAPIView):
    serializer_class = TimelineSerializer
    permission_classes = [IsAuthenticated]
    queryset = Timeline.objects.all()
