from django.urls import path

from notifications.views import NotificationView

urlpatterns = [
    path("notifications/", NotificationView.as_view()),
    path("notifications/<int:id>/mark_read/", NotificationView.as_view()),
]
