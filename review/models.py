from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from user.models import User
from product.models import Product


class Review(models.Model):
    body = models.TextField('리뷰 내용')
    image = models.ImageField('리뷰 이미지', blank=True, upload_to='review//%Y/%m/%d')
    review = models.PositiveIntegerField('리뷰 평점', validators=[MinValueValidator(0), MaxValueValidator(5)])

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review_product')

    reg_date = models.DateTimeField('등록 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return self.body
