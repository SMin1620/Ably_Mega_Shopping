from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', '남성'
        FEMALE = 'F', '여성'

    first_name = None
    last_name = None
    date_joined = None

    name = models.CharField('이름', max_length=50)
    gender = models.CharField('성별', max_length=1, blank=True, choices=GenderChoices.choices)

    reg_date = models.DateTimeField('생성 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f'{self.id}, {self.username}, {self.name}'
