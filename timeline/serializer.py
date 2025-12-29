from rest_framework import serializers

from timeline.models import Timeline


class TimelineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timeline
        fields = ['event_type', 'project', 'time']
        
    def validate_event(self, value):
        if not value:
            raise serializers.ValidationError("Event cannot be empty")
        return value
