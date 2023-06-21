from django.db import models

from account.models import User


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_post")
    kind = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=255)
    registered_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)
    video = models.FileField(upload_to="post_videos/", null=True, blank=True)
    recommendation = models.IntegerField()
