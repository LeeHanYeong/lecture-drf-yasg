from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:20]
