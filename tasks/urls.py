from django.urls import path

from tasks.views import TaskView, TaskViewDetail


urlpatterns = [
    path("tasks/", TaskView.as_view()),
    path("tasks/<int:id>/", TaskViewDetail.as_view()),
]
