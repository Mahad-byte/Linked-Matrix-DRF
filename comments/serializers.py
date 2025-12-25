from rest_framework import serializers
from comments.models import Comment
from users.models import User
from tasks.models import Task
from project.models import Project


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(), allow_null=True, required=False)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'created_at', 'task', 'project']
        read_only_fields = ['created_at']

    def validate_text(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Comment text cannot be empty.")
        return value

    def create(self, validated_data):
        # Any comment-related business rules can go here later.
        return super().create(validated_data)

