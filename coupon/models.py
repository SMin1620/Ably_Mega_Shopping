from django.db import models

from user.models import User


class Coupon(models.Model):
    name = models.CharField('쿠폰 이름', max_length=100)
    discount_price = models.DecimalField('쿠폰 가격', max_digits=10, decimal_places=2, null=True, blank=True)
    discount_percent = models.DecimalField('쿠폰 퍼센트', max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField('쿠폰 수량', default=0)

    user = models.ManyToManyField(User, through='coupon.CouponUser', related_name='coupon_user')

    reg_date = models.DateTimeField('등록 날짜', auto_now_add=True)

    class Meta:
        db_table = 'coupon'

    def __str__(self):
        return self.name


class CouponUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)

    reg_date = models.DateTimeField('발급일', auto_now_add=True)

    class Meta:
        db_table = 'coupon_user'

    def __str__(self):
        return f'{self.user.username}, {self.coupon}'
