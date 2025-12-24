from django.contrib import admin
from project.models import Project
from profiles.models import Profile
from tasks.models import Task

# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Task)


