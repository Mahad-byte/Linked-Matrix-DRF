from django.shortcuts import render
from rest_framework.views import APIView
from timeline.serializer import TimelineSerializer
from timeline.models import Timeline
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class TimelineView(APIView):
    serializer_class = TimelineSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        queryset = Timeline.objects.all()
        serializer = TimelineSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
 