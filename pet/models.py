from django.db import models


# Create your models here.
class Personality(models.Model):
    activity = models.CharField(max_length=1)  # A: 모험, L: 안주 (활동성)
    relationship = models.CharField(max_length=1)  # E: 외향, I: 내향 (관계성)
    proto_dog = models.CharField(max_length=1)  # C: 교감, W: 본능 (야생성)
    dependence = models.CharField(max_length=1)  # T: 신뢰, N: 필요 (의존성)


class Pet(models.Model):
    gender = models.CharField(max_length=1)  # W: 여자, M: 남자
    owner_name = models.CharField(max_length=15)
    birth_day = models.DateField()
    meet_day = models.DateField()
    name = models.CharField(max_length=15)
    kind = models.CharField(max_length=3)  # Cat: 고양이, Dog: 강아지
    personality = models.OneToOneField(Personality, on_delete=models.CASCADE)
