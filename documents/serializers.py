from rest_framework import serializers

from documents.models import Document
from project.models import Project


class DocumentSerializer(serializers.ModelSerializer):
    # Accept the primary key and validate it against Project
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Document
        fields = ['id', 'name', 'description', 'file', 'version', 'project']

    def validate_file(self, value):
        if not value:
            raise serializers.ValidationError("File is required.")
        return value

    def create(self, validated_data):
        if not validated_data.get('version'):
            validated_data['version'] = '1.0'
        return super().create(validated_data)
