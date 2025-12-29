from django.urls import path

from comments.views import CommentView, CommentDetailAPI


urlpatterns = [
    path("comments/", CommentView.as_view()),
    path("comments/<int:id>/", CommentDetailAPI.as_view()),
]
