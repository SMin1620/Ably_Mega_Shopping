from rest_framework import serializers
from django.db import transaction
from django.db.models import F

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
            'quantity',
            'reg_date',
            'user'
        ]


class CouponUserSerializer(serializers.ModelSerializer):
    """
    유저 쿠폰 발급
    """
    user = serializers.ReadOnlyField(source='user.username')
    coupon = serializers.IntegerField(required=True)

    class Meta:
        model = CouponUser
        fields = [
            'id',
            'user',
            'coupon',
            'reg_date'
        ]

    # 동시성 문제를 해결하기 위해 트랜잭션 설정
    @transaction.atomic()
    def create(self, validated_data, *args, **kwargs):
        Coupon.objects.filter(
            pk=validated_data.get('coupon'),
        ).update(quantity=F('quantity') - 1)

        coupon_user = CouponUser.objects.create(
            user=self.context['request'].user,
            coupon_id=validated_data.get('coupon'),
        )
        return coupon_user
