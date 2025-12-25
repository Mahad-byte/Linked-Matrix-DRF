from rest_framework import serializers
from tasks.models import Task
from project.models import Project
from profiles.models import Profile


class TaskSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    asignee = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'project', 'asignee']
        read_only_fields = ['id']

    def validate_title(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Task title cannot be empty.")
        return value

    def create(self, validated_data):
        if not validated_data.get('status'):
            validated_data['status'] = 'todo'
        return super().create(validated_data)
