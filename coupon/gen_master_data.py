from coupon.models import Coupon


def gen_master(apps, schema_editor):
    Coupon(name='가입 축하 쿠폰', discount_percent=20, quantity=100).save()
    Coupon(name='배송비 할인 쿠폰', discount_price=2000, quantity=100).save()
    Coupon(name='추석 연휴 할인', discount_percent=10, quantity=100).save()