from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from user.models import User
from product.models import ProductReal


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_real = models.ForeignKey(ProductReal, on_delete=models.CASCADE)

    quantity = models.PositiveSmallIntegerField('수량', default=1,
                                                validators=[MinValueValidator(1), MaxValueValidator(100)])

    reg_date = models.DateTimeField('생성 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)

    class Meta:
        db_table = 'cart'

    def __str__(self):
        return f'id : {self.id} / user : {self.user} / product : {self.product_real} / quantity : {self.quantity}'
