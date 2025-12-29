from django.db import models

from profiles.models import Profile
from users.models import User


# Create your models here.
class Project(models.Model):
    title = models.CharField()
    description = models.CharField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="projects", default=2
    )
    team_members = models.ManyToManyField(Profile, related_name="project_team")

    def __str__(self):
        return self.title
