from django.contrib import admin
from project.models import Project
from profiles.models import Profile
from tasks.models import Task
from timeline.models import Timeline
from notifications.models import Notification


# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(Timeline)
admin.site.register(Notification)


