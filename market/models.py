from django.db import models

from user.models import User


# Create your models here.
class Market(models.Model):
    name = models.CharField('마켓 이름', max_length=100)
    site_url = models.URLField('마켓 사이트', max_length=100)
    email = models.EmailField('마켓 이메일', max_length=100)
    description = models.TextField('마켓 설명')

    review_point = models.DecimalField('리뷰 포인트', max_digits=2, decimal_places=1, default=0)

    master = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'market'

    def __str__(self):
        return f'{self.id}, {self.name}, {self.master}'

