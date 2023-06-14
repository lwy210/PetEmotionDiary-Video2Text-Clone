from django.db import models

from account.models import User
from post.models import Post


# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comment"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    registered_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    recommendation = models.IntegerField()
