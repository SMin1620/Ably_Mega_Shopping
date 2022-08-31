from rest_framework import mixins, viewsets, status

from coupon.models import Coupon, CouponUser
from coupon.serializers import (
    CouponSerializer,
    CouponUserSerializer
)


class CouponListDetailViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.CreateModelMixin,
                              viewsets.GenericViewSet):
    """
    쿠폰 리스트, 디테일 뷰셋
    """
    lookup_url_kwarg = 'coupon_id'

    def get_queryset(self):
        if self.request.method == 'GET':
            return Coupon.objects.all()
        else:
            return CouponUser.objects.alL()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CouponSerializer
        else:
            return CouponUserSerializer

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            coupon_id=self.kwargs['coupon_id']
        )


