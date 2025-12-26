from django.db import models

from users.models import User
from tasks.models import Task
from project.models import Project


# Create your models here.
class Comment(models.Model):
    text = models.CharField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_author')
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_comment')
    project = models.ForeignKey(Project, 
                                on_delete=models.CASCADE, 
                                related_name='project_comment'
    )
