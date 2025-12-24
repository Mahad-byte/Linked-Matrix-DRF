from django.db import models

# Create your models here.
class Profile(models.Model):
    picture = models.ImageField()
    role = models.CharField(
        choices={
            'M':'Manager',
            'QA':'Quality Assaurance',
            'Dev':'Developer'
        },
        default='dev'
    )
    contact_number = models.CharField(
        max_length=11
    )
