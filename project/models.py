from django.db import models
from profiles.models import Profile


# Create your models here.
class Project(models.Model):
    title = models.CharField()
    description = models.CharField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    team_members = models.ManyToManyField(Profile, related_name='project_team') #check

    def __str__(self):
        return self.title