from django.contrib import admin

from comments.models import Comment
from documents.models import Document
from notifications.models import Notification
from profiles.models import Profile
from project.models import Project
from tasks.models import Task
from timeline.models import Timeline
from users.models import User

# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(Timeline)
admin.site.register(Notification)
admin.site.register(Document)
admin.site.register(Comment)
admin.site.register(User)
