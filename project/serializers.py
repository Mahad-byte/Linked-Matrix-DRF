from rest_framework import serializers
from project.models import Project
from profiles.models import Profile


class ProjectSerializer(serializers.ModelSerializer):
    # team_members = serializers.PrimaryKeyRelatedField(
    #     queryset=Profile.objects.all(), many=True
    # )
    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'team_members']   
