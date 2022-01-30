from django.db import models

from django.contrib.auth.models import User



class NewsPost(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='news_posts')
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    content = models.TextField()
    image = models.ImageField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title
