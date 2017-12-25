
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, related_name='blog_posts')
    # author = models.ForeignKey(User, related_name='mycomment', verbose_name = u'评论人')
    # author = models.ForeignKey(User)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Mata:
        ordering = ("-publish", )

    def __str__(self):
        return self.title