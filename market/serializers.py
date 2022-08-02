from rest_framework import serializers

from market.models import Market
from product.models import Product, ProductReal


class MarketListSerializer(serializers.ModelSerializer):
    """
    마켓 목록 조회 - 사용자 전용
    """
    class Meta:
        model = Market
        fields = [
            'id',
            'name',
            'review_point',
            'site_url'
        ]


class MarketDetailSerializer(serializers.ModelSerializer):
    """
    마켓 상세 조회 - 사용자 전용
    """
    class Meta:
        model = Market
        fields = [
            'id',
            'name',
            'site_url',
            'description',
            'email',
            'review_point',
            'master'
        ]


class MarketProductListSerializer(serializers.ModelSerializer):
    """
    마켓별 상품 리스트 시리얼라이저 - 사용자 전용
    """
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
            'review_count',
            'review_point',
            'product_like_user',
            'market',
            'category',
        ]