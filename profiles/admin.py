from django.contrib import admin

from project.models import Project
from profiles.models import Profile
from tasks.models import Task
from timeline.models import Timeline
from documents.models import Document
from comments.models import Comment
from notifications.models import Notification


# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(Timeline)
admin.site.register(Notification)
admin.site.register(Document)
admin.site.register(Comment)
