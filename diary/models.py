from django.db import models

from account.models import User
from pet.models import Pet

# Create your models here.


class Keyword(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word


class Diary(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_diary")
    registered_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=255)
    video = models.CharField(max_length=45)
    day = models.DateField()
    thumbnail = models.CharField(max_length=45)
    bookmark = models.BooleanField(default=False)
    keywords = models.ManyToManyField(Keyword)

    def __str__(self):
        return str(self.day) + ": " + self.pet.name + "의 일기"
