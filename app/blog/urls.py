from django.urls import path

from . import apis

urlpatterns = [
    path('posts/', apis.PostListCreateAPIView.as_view()),
    path('comments/', apis.CommentListCreateAPIView.as_view()),
]
