from django.db import models


# Create your models here.
class Post(models.Model):
    post_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    content = models.CharField(max_length=255)
    registered_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    recommendation = models.IntegerField()
