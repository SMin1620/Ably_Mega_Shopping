from django.db import transaction
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from market.models import Market
from product.models import Product, ProductReal


class MarketAdminProductRealListCreateSerializer(serializers.ModelSerializer):
    """
    상품 옵션 시리얼라이저
    """
    class Meta:
        model = ProductReal
        fields = [
            'id',
            'reg_date',
            'update_date',
            'is_hidden',
            'is_sold_out',
            'add_price',
            'stock_quantity',
            'product',
            'option_1_name',
            'option_1_display_name',
            'option_2_name',
            'option_2_display_name',
        ]
        extra_kwargs = {
            'option_1_name': {'required': False, 'allow_null': True, "write_only": True},
            'option_1_display_name': {'required': False, 'allow_null': True, "write_only": True},
            'option_2_name': {'required': False, 'allow_null': True,"write_only": True},
            'option_2_display_name': {'required': False, 'allow_null': True, "write_only": True},
            'add_price': {'required': False, 'allow_null': True, "write_only": True},
            'stock_quantity': {'required': False, 'allow_null': True, "write_only": True},
            'is_hidden': {'required': False, 'allow_null': True, "write_only": True},
            'is_sold_out': {'required': False, 'allow_null': True, "write_only": True},
        }


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
            'site_url',
            'master'
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
    market = serializers.ReadOnlyField(source='market.id')

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


class MarketAdminDetailSerializer(serializers.ModelSerializer):
    """
    해당 마켓의 상품 상세 조회 - 마켓 관리자 전용
    """
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'name',
            'display_name',
            'description',
            'price',
            'sale_price',
            'is_hidden',
            'is_sold_out',
            'hit_count',
            'review_count',
            'review_point',
            'reg_date',
            'update_date',
            'delete_date',
            'category',
            'market',
        ]


class MarketAdminProductRealSerializer(serializers.ModelSerializer):
    """
    상품의 옵션 생성 시리얼라이저 - 마켓 관리자 전용
    """
    def validate(self, data):
        product = data.get('product', None)

        if product and ProductReal.objects.filter(
            product=data['product'],
            option_1_name=data['option_1_name'],
            option_2_name=data['option_2_name']
        ).exists():
            raise serializers.ValidationError(
                _('product and option_1_name and option_2_name should be unique together')
            )
        return data

    class Meta:
        model = ProductReal
        fields = [
            'id',
            'product',
            'option_1_display_name',
            'option_1_name',
            'option_2_display_name',
            'option_2_name',
            'is_hidden',
            'add_price',
            'stock_quantity',
            'rgb_color'
        ]
        extra_kwargs = {
            'product': {'required': False, 'allow_null': True},
        }


class MarketAdminProductListCreateSerializer(serializers.ModelSerializer):
    """
    삼품 생성 (옵션 포함) 시리얼라이저 - 마켓 관리자 전용
    """
    product_reals = MarketAdminProductRealSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'display_name',
            'description',
            'price',
            'sale_price',
            'review_count',
            'review_point',
            'product_like_user',
            'market',
            'category',
            'product_reals'
        ]
        read_only_fields = [
            'market',
            'review_count',
            'review_point',
            'product_like_user',
        ]

    @transaction.atomic
    def create(self, validated_data):
        product_reals = validated_data.pop('product_reals', [])
        product = Product.objects.create(**validated_data)

        product_reals = list(map(lambda product_real: {**product_real, "product": product.id}, product_reals))

        for product_real in product_reals:
            product_real_serializer = MarketAdminProductRealSerializer(data=product_real)

            product_real_serializer.is_valid(raise_exception=True)
            product_real_serializer.save()

        return product


class MarketAdminUpdateDeleteSerializer(serializers.ModelSerializer):
    """
    본인 마켓의 상품 수정 - 마켓 관리자 전용
    """

    class Meta:
        model = Product
        fields = [
            'name',
            'display_name',
            'description',
            'price',
            'sale_price',
            'is_hidden',
            'is_sold_out',
            'category',
        ]



