from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Profile(models.Model):
    picture = models.ImageField()
    role = models.CharField(
        choices={"M": "Manager", "QA": "Quality Assaurance", "Dev": "Developer"},
        default="dev",
    )
    contact_number = models.CharField(max_length=11)
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="user_profile",
        default=2,
    )
