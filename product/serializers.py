from rest_framework import serializers

from product.models import (
    Product,
    ProductReal,
    Category
)


class CategorySerializer(serializers.ModelSerializer):
    """
    카테고리 시리얼라이저
    """
    class Meta:
        model = Category
        fields = [
            'id',
            'name'
        ]


class ProductRealSerializer(serializers.ModelSerializer):
    """
    상품 옵션 시리얼라이저
    """
    class Meta:
        model = ProductReal
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    """
    상품 리스트 조회 시리얼라이저- 사용저 전용
    """
    class Meta:
        model = Product
        fields = [
            'id',
            'display_name',
            'price',
            'sale_price',
            'is_sold_out',
            'hit_count',
            'review_count',
            'review_point',
            'market',
            'category',
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    """
    상품 디테일 조회 시리얼라이저 - 사용자 전용
    """
    product_real = ProductRealSerializer(many=True, read_only=True)
    product_like_user = serializers.SerializerMethodField(read_only=True)

    def get_product_like_user(self, obj):
        return obj.product_like_user.count()

    class Meta:
        model = Product
        fields = [
            'id',
            'display_name',
            'price',
            'sale_price',
            'is_hidden',
            'is_sold_out',
            'reg_date',
            'update_date',
            'product_like_user',
            'hit_count',
            'review_count',
            'review_point',
            'category',
            'market',
            'product_real',
        ]


