from rest_framework import serializers

from product.models import (
    Product,
    ProductReal,
    Category
)
from market.serializers import MarketListSerializer


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


# class ProductSerializer(serializers.ModelSerializer):
#     """
#     상품 시리얼라이저
#     """
#     category = CategorySerializer()
#     market = MarketListSerializer()
#     product_real = ProductRealSerializer(many=True)
#
#     class Meta:
#         model = Product
#         fields = [
#             'id',
#             'name',
#             'display_name',
#             'description',
#             'price',
#             'sale_price',
#             'is_hidden',
#             'is_sold_out',
#             'is_deleted',
#             'reg_date',
#             'update_date',
#             'delete_date',
#             'hit_count',
#             'review_count',
#             'review_point',
#             'category',
#             'market',
#             'product_real',
#         ]


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
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    """
    상품 디테일 조회 시리얼라이저 - 사용자 전용
    """
    category_name = serializers.SerializerMethodField(read_only=True)
    display_name = serializers.SerializerMethodField(read_only=True)
    description = serializers.SerializerMethodField(read_only=True)
    price = serializers.SerializerMethodField(read_only=True)
    sale_price = serializers.SerializerMethodField(read_only=True)
    is_sold_out = serializers.SerializerMethodField(read_only=True)
    hit_count = serializers.SerializerMethodField(read_only=True)
    review_count = serializers.SerializerMethodField(read_only=True)
    review_point = serializers.SerializerMethodField(read_only=True)

    def get_category_name(self, obj):
        return obj.product.category.name

    def get_display_name(self, obj):
        return obj.product.display_name

    def get_description(self, obj):
        return obj.product.description

    def get_price(self, obj):
        return obj.product.price

    def get_sale_price(self, obj):
        return obj.product.sale_price

    def get_is_sold_out(self, obj):
        return obj.product.is_sold_out

    def get_hit_count(self, obj):
        return obj.product.hit_count

    def get_review_count(self, obj):
        return obj.product.review_count

    def get_review_point(self, obj):
        return obj.product.review_point

    class Meta:
        model = ProductReal
        fields = [
            'category_name',
            'display_name',
            'description',
            'price',
            'sale_price',
            'is_sold_out',
            'hit_count',
            'review_count',
            'review_point',
            'option_1_type',
            'option_1_display_name',
            'option_2_type',
            'option_2_display_name',
            'option_3_type',
            'option_3_display_name',
        ]


