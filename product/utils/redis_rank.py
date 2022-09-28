import os

import django
from django.core.cache import cache

from product.models import Product


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

"""
redis를 이용한 상품 랭킹 산출
"""

def set_rank():
    products = Product.objects.all()
    data = []

    for product in products:
        review_point = product.review_point
        if review_point != 0:
            data.append({"review_point": review_point})
    rank_data = sorted(data, key=(lambda x: x["review_point"]), reverse=True)
    return rank_data


def create_rank():
    data = set_rank()
    # 테스트 용으로 expire time을 10분으로 설정
    cache.set("rank", data, 600)
    rank = cache.get("rank")
    return rank


def get_rank():
    rank = cache.get("rank")
    if rank is None:
        rank = create_rank()
    return rank








