from rest_framework import serializers

from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["id", "text", "created_at", "user", "mark_read"]

    def validate_text(self, value):
        if not value:
            raise serializers.ValidationError("Text cannot be empty")
        return value
