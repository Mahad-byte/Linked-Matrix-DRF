from django.db import models
from project.models import Project

# Create your models here.
class Document(models.Model):
    name = models.CharField()
    description = models.CharField()
    file = models.FileField(upload_to='DRF/')
    version = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_document')
