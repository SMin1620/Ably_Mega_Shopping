from rest_framework import serializers

from cart.models import CartItem


class CartSerializer(serializers.ModelSerializer):
    """
    장바구니 시리얼라이저
    """
    class Meta:
        model = CartItem
        fields = [
            'id',
            'user',
            'product_real',
            'quantity',
            'reg_date',
            'update_date'
        ]


class CartCreateSerializer(serializers.ModelSerializer):
    """
    장바구니 생성 시리얼라이저
    """
    class Meta:
        model = CartItem
        fields = [
            'id',
            'user',
            'product_real',
            'quantity',
            'reg_date',
            'update_date'
        ]
        read_only_fields = [
            'id',
            'user',
        ]


class CartDetailUpdateDeleteSerializer(serializers.ModelSerializer):
    """
    장바구니 상세조회, 수정, 삭제 시리얼라이저
    """
    class Meta:
        model = CartItem
        fields = [
            'id',
            'user',
            'product_real',
            'quantity',
            'reg_date',
            'update_date'
        ]
        read_only_fields = [
            'id',
            'user',
        ]

