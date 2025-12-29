from django.db import models

from profiles.models import Profile
from project.models import Project


# Create your models here.
class Task(models.Model):
    title = models.CharField()
    description = models.CharField()
    status = models.CharField(
        choices={
            "O": "Open",
            "R": "Review",
            "W": "Working",
            "AR": "Awaiting Release",
            "WQA": "Waiting QA",
        },
        default="Open",
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_tasks"
    )
    asignee = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="profile_tasks"
    )

    def __str__(self):
        return f"{self.title}, {self.description}"
