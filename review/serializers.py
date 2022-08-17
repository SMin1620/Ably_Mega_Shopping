from rest_framework import serializers

from review.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'body',
            'review',
            'user',
            'product',
            'reg_date',
            'update_date'
        ]


class ReviewCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = [
            'id',
            'body',
            'review',
            'user',
            'product',
            'reg_date',
            'update_date'
        ]
        read_only_fields = [
            'id',
            'user',
            'reg_date',
            'update_date'
        ]

