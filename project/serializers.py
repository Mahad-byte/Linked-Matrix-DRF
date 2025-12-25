from rest_framework import serializers
from project.models import Project
from profiles.models import Profile


class ProjectSerializer(serializers.ModelSerializer):
    team_members = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), many=True, required=False)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'team_members']
        read_only_fields = ['id', 'start_date', 'end_date']

    def validate_title(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Project title cannot be empty.")
        return value

    def create(self, validated_data):
        members = validated_data.pop('team_members', [])
        project = Project.objects.create(**validated_data)
        if members:
            project.team_members.set(members)
        return project
