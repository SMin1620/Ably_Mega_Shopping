from django.contrib import admin

from coupon.models import Coupon, CouponUser


admin.site.register(Coupon)
admin.site.register(CouponUser)