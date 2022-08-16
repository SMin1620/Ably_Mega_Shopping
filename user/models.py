from django.db import models
from django.shortcuts import resolve_url
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
    profile_img = models.ImageField('프로필 이미지', blank=True, upload_to='user/profile_img/%Y/%m/%d',
                                    help_text="gif/png/jpg 이미지를 업로드해주세요.")

    reg_date = models.DateTimeField('생성 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f'{self.id}, {self.username}, {self.name}'

    @property
    def profile_img_url(self) -> str:
        if self.profile_img:
            return self.profile_img.url
        return resolve_url('pydenticon_image', data=self.username)


