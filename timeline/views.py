from django.shortcuts import render
from rest_framework.views import APIView
from timeline.serializer import TimelineSerializer
from timeline.models import Timeline
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
class TimelineView(APIView):
    serializer_class = TimelineSerializer
    
    def get(self, request):
        queryset = Timeline.objects.all()
        print("queryset: ", queryset)
        serializer = TimelineSerializer(queryset, many=True)
        print("timeline events: ", serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
        