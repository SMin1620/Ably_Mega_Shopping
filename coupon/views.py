from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # serializer의 create() 함수 호출
        # 트랜잭션 시작
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


