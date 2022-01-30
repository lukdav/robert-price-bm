from django.db import models

from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
    title = models.CharField(max_length=150, unique=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    article = models.TextField()

    def __str__(self):
        return self.title

