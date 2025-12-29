from django.db import models
from django.contrib.auth.models import AbstractUser

from users.custommanager import CustomUserManager


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )
    phone_number = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    # Field Properties
    @property
    def display_name(self):
        return f"{self.first_name}-$"

    def __str__(self):
        return f"{self.email}"

    # Meta (Inner Class)
    class Meta:
        verbose_name = "User"
        ordering = ["-created_at"]
