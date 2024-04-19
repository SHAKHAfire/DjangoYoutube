from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):
    title: str = models.CharField(max_length=255)
    content: str = models.TextField()
    author: User = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    created: datetime = models.DateTimeField(auto_now_add=True)
    time_updated: datetime = models.DateTimeField(auto_now=True)
    objects = models.Manager()  # default

    def __str__(self):
        return self.title


class PostComment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    content: str = models.TextField()
    created: datetime = models.DateTimeField(auto_now_add=True)
    author: User = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.post} - {self.author}"
