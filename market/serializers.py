from rest_framework import serializers

from market.models import Market


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