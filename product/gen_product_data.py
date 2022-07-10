from product.models import (
    Category,
    Product
)


def gen_category():
    """
    카테고리 더미데이터
    """

    Category(name='구두').save()
    Category(name='니트').save()
    Category(name='롱스커트').save()
    Category(name='숏스커트').save()
    Category(name='청바지').save()
    Category(name='청자켓').save()
    Category(name='청치마').save()
    Category(name='코트').save()
    Category(name='백').save()
    Category(name='블라우스').save()


def gen_product(
        name: str,
        display_name: str,
        description: str,
        price: int,
        sale_price: int,
        is_hidden: bool,
        is_sole_out: bool,
        is_deleted: bool,
        hit_count: int,
        review_count: int,
        review_point: int,
) -> None:
    """
    상품 설정
    """
    category_id = Category.objects.filter(name=name).first().id

    product = Product(
        name=name,
        display_name=display_name,
        description=description,
        price=price,
        sale_price=sale_price,
        is_hidden=is_hidden,
        is_sold_out=is_sole_out,
        is_deleted=is_deleted,
        hit_count=hit_count,
        review_count=review_count,
        review_point=review_point,
        category_id=category_id
    )

    product.save()


def gen_product_data(apps, schema_editor):
    """
    상품 더미데이터
    """

    gen_category()

    gen_product(
        '구두',
        '인스타 셀럽 구두',
        '트렌드에 맞는 상품입니다.',
        20000,
        18000,
        False,
        False,
        False,
        1000,
        250,
        4,
    )

    gen_product(
        '니트',
        '브이넥 아가일 니트',
        '두께감이 어느정도 있는 니트입니다.',
        70000,
        63000,
        False,
        False,
        False,
        400,
        50,
        3,
    )

    gen_product(
        '롱스커트',
        '체크무늬 트렌트 롱스커트',
        '롱스커트입니다.',
        30000,
        27000,
        False,
        False,
        False,
        100,
        20,
        4,
    )

    gen_product(
        '숏스커트', '인스타 셀럽 숏스커트', '연예인이 착용한 스커트입니다.',
        30000, 30000, False, False, False, 3000, 550, 5
    )

    gen_product(
        '청바지', '인스타 셀럽 청바지', '와일드 핏의 청버자입니다.',
        80000, 70000, False, False, False, 100, 10, 3
    )

    gen_product(
        '청자켓', '인스타 셀럽 청자켓', '연예인이 착용한 자켓입니다.',
        30000, 30000, False, False, False, 3000, 550, 5
    )






