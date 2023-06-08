from django.db import models

from post.models import Post


# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    registered_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    recommendation = models.IntegerField()
