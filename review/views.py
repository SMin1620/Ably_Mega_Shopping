from rest_framework import viewsets, mixins, status

from review.models import Review
from review.serializers import (
    ReviewSerializer,
    ReviewCreateSerializer,
)


class ReviewListCreateViewSet(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              viewsets.GenericViewSet):
    """
    리뷰 조회, 생성 뷰
    """
    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Review.objects \
            .filter(product_id=product_id) \
            .all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewSerializer
        else:
            return ReviewCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)