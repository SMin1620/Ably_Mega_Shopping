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
            'reg_date'
        ]
