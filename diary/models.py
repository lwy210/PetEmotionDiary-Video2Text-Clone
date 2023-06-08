from django.db import models

from pet.models import Pet


# Create your models here.
class Diary(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    registered_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    content = models.CharField(max_length=255)
    video = models.CharField(max_length=45)
    day = models.DateField()
    thumbnail = models.CharField(max_length=45)
    bookmark = models.BooleanField(default=False)
