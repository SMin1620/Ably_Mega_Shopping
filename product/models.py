from django.db import models


class Category(models.Model):
    """
    카테고리 모델
    """

    name = models.CharField('카테고리명', max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return f'{self.id}, {self.name}'


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

    class Meta:
        db_table = 'product'

    def __str__(self):
        return f'{self.id}, {self.name}'








