from django.db import models

from users.models import User


# Create your models here.
class Notification(models.Model):
    text = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_notify')
    created_at = models.DateTimeField(auto_now_add=True)
    mark_read = models.BooleanField(default=False)
