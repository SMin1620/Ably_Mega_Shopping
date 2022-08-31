from rest_framework import serializers

from coupon.models import Coupon, CouponUser


class CouponSerializer(serializers.ModelSerializer):
    """
    쿠폰 시리얼라이저
    """
    class Meta:
        model = Coupon
        fields = [
            'id',
            'name',
            'discount_price',
            'discount_percent',
            'reg_date',
            'user'
        ]


class CouponUserSerializer(serializers.ModelSerializer):
    """
    유저 쿠폰 발급
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = CouponUser
        fields = [
            'id',
            'user',
            'coupon',
            'reg_date'
        ]
        read_only_fields = [
            'id',
            'user',
            'coupon',
            'reg_date'
        ]