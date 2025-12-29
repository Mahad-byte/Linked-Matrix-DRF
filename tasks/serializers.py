from rest_framework import serializers

from profiles.models import Profile
from project.models import Project
from project.serializers import ProjectSerializer
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    asignee = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())

    # Seperate write for nested serializer relation
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(), source="project", write_only=True
    )

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "project_id",
            "project",
            "asignee",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Task title cannot be empty.")
        return value

    def create(self, validated_data):
        validated_data.pop("project")
        if not validated_data.get("status"):
            validated_data["status"] = "todo"
        return super().create(validated_data)
