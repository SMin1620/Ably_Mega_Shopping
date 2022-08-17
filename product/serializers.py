from rest_framework import serializers

from product.models import (
    Product,
    ProductReal,
    Category,
    ProductLikeUser
)
from review.models import Review
from qna.serializers import QuestionSerializer


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


class ProductLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLikeUser
        fields = [
            'id',
            'product',
            'user'
        ]
        read_only_fields = [
            'id',
            'product',
            'user'
        ]


class ProductListSerializer(serializers.ModelSerializer):
    """
    상품 리스트 조회 시리얼라이저- 사용저 전용
    """
    market = serializers.SerializerMethodField(read_only=True)
    review_count = serializers.SerializerMethodField(read_only=True)
    review_point = serializers.SerializerMethodField(read_only=True)

    def get_market(self, obj):
        return obj.market.name

    def get_review_count(self, obj):
        return Review.objects.filter(product=obj).count()

    def get_review_point(self, obj):
        reviews = Review.objects.filter(product=obj)
        if len(reviews) > 0:
            total_point = 0
            for review in reviews:
                total_point += review.review
            avg_point = total_point / len(reviews)
            return avg_point
        else:
            return None

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
            'thumb_img_url'
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    """
    상품 디테일 조회 시리얼라이저 - 사용자 전용
    """
    product_real = ProductRealSerializer(many=True, read_only=True)
    product_like_user = serializers.SerializerMethodField(read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)
    review_count = serializers.SerializerMethodField(read_only=True)
    review_point = serializers.SerializerMethodField(read_only=True)

    def get_product_like_user(self, obj):
        return obj.product_like_user.count()

    def get_review_count(self, obj):
        return Review.objects.filter(product=obj).count()

    def get_review_point(self, obj):
        reviews = Review.objects.filter(product=obj)
        if len(reviews) > 0:
            total_point = 0
            for review in reviews:
                total_point += review.review
            avg_point = total_point / len(reviews)
            return avg_point
        else:
            return None

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
            'questions',
            'thumb_img_url',
        ]


