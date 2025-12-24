from django.db import models
from project.models import Project

# Create your models here.
class Timeline(models.Model):
    event_type = models.CharField(
        choices={
            'C':'created',
            'U':'updated',
            'D':'deleted',
        }
    )
    time = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_timeline')
