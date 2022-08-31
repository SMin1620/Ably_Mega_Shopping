from rest_framework import mixins, viewsets, status

from coupon.models import Coupon, CouponUser
from coupon.serializers import CouponSerializer


class CouponListDetailViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    """
    쿠폰 리스트, 디테일 뷰셋
    """
    lookup_url_kwarg = 'coupon_id'

    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
