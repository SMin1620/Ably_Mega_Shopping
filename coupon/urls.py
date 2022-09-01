from django.urls import path

from coupon.views import (
    CouponListDetailViewSet,
    CouponUserSerializer
)


coupon_list = CouponListDetailViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

coupon_detail = CouponListDetailViewSet.as_view({
    'get': 'retrieve',
})


urlpatterns = [
    path('', coupon_list, name='쿠폰 목록'),
    path('<int:coupon_id>/', coupon_detail, name='쿠폰 상세'),

]