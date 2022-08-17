from django.db import models

from market.models import Market
from user.models import User


class Category(models.Model):
    """
    카테고리 모델
    """

    name = models.CharField('카테고리명', max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return f'{self.name}'


# Create your models here.
class Product(models.Model):
    """
    상품 모델
    """

    name = models.CharField('상품명(내부용)', max_length=100)
    display_name = models.CharField('상품명(노출용)', max_length=100)
    description = models.TextField('상품 설명')

    price = models.PositiveIntegerField('권장 판매가', default=0)
    sale_price = models.PositiveIntegerField('실제 판매가', default=0)

    is_hidden = models.BooleanField('숨김 여부', default=False)
    is_sold_out = models.BooleanField('품절 여부', default=False)
    is_deleted = models.BooleanField('삭제 여부', default=False)

    delete_date = models.DateTimeField('삭제 날짜', null=True, blank=True)
    reg_date = models.DateTimeField('생성 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)

    hit_count = models.PositiveIntegerField('조회수', default=0)
    review_count = models.PositiveIntegerField('리뷰수', default=0)
    review_point = models.PositiveIntegerField('리뷰 평점', default=0)

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    market = models.ForeignKey(Market, on_delete=models.DO_NOTHING)

    product_like_user = models.ManyToManyField(
        User,
        through='product.ProductLikeUser',
        related_name='product_like_user'
    )

    class Meta:
        db_table = 'product'

    def __str__(self):
        return f'{self.id}, {self.name}'

    @property
    def thumb_img_url(self):
        img_name = self.category.name
        img_name += '2' if self.id % 2 == 0 else ''

        return f"https://raw.githubusercontent.com/SMin1620/mbly-img/master/{img_name}.jpg"


class ProductReal(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_real')

    option_1_type = models.CharField('옵션1 타입', max_length=10, default='SIZE')
    option_1_name = models.CharField('옵션1 이름 (내부용)', max_length=30)
    option_1_display_name = models.CharField('옵션1 이름 (노출용)', max_length=30)

    option_2_type = models.CharField('옵션2 타입', max_length=10, default='COLOR')
    option_2_name = models.CharField('옵션2 이름 (내부용)', max_length=30)
    option_2_display_name = models.CharField('옵션2 이름 (노출용)', max_length=30)

    option_3_type = models.CharField('옵션3 타입', max_length=10, default='', blank=True)
    option_3_name = models.CharField('옵션3 이름 (내부용)', max_length=30, blank=True)
    option_3_display_name = models.CharField('옵션3 이름 (노출용)', max_length=30, blank=True)

    reg_date = models.DateTimeField('생성 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)

    is_hidden = models.BooleanField('숨김 여부', default=False)
    is_sold_out = models.BooleanField('품절 여부', default=False)

    add_price = models.PositiveIntegerField('추가 가격', default=0)

    stock_quantity = models.PositiveIntegerField('재고량', default=0)


    class Meta:
        db_table = 'product_real'
        constraints = [
            models.UniqueConstraint(
                'product',
                'option_1_name',
                'option_2_name',
                'option_3_name',
                name='option_name_unique'
            ),
        ]

    def __str__(self):
        return f'{self.id}, {self.option_1_display_name} - {self.option_2_display_name} - {self.option_3_display_name}'

    @property
    def rgb_color(self):
        return ProductReal.rgb_color_from_color_name(self.option_2_name)

    @classmethod
    def rgb_color_from_color_name(cls, color):
        if color == '레드':
            rgb_color = 'FF0000'
        elif color == '그린':
            rgb_color = '008000'
        elif color == '블루':
            rgb_color = '0000FF'
        elif color == '핑크':
            rgb_color = 'ffc0cb'
        elif color == '와인':
            rgb_color = '722F37'
        else:
            rgb_color = 'FFFFFF'

        return rgb_color


class ProductLikeUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    reg_date = models.DateTimeField('생성 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)

    class Meta:
        db_table = 'product_like_user'

    def __str__(self):
        return f'{self.user.username} // {self.product.name}'

