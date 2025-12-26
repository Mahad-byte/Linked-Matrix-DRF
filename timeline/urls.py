from django.urls import path
from timeline.views import TimelineView


urlpatterns = [
    path('timeline/', TimelineView.as_view()),
]
