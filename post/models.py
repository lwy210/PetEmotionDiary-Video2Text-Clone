from django.db import models


# Create your models here.
class Post(models.Model):
    kind = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=255)
    registered_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    image = models.CharField(max_length=45)
    video = models.CharField(max_length=45)
    recommendation = models.IntegerField()
