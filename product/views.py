from rest_framework import mixins, viewsets
from rest_framework.decorators import action

from product.models import (
    Product,
    ProductReal,
    Category
)
from product.serializers import (
    CategorySerializer,
    ProductListSerializer,
    ProductDetailSerializer,
)


# Create your views here.
class ProductListAPI(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    상품 리스트 조회 및 생성 뷰 - 사용자 전용
    """

    lookup_url_kwarg = 'product_id'

    def get_queryset(self):
        if self.action == 'list':
            return Product.objects.all()
        else:
            return ProductReal.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        else:
            return ProductDetailSerializer


class CategoryProductListViewSet(mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin,
                                 viewsets.GenericViewSet):
    """
    카테고리별 상품 리스트 조회 - 사용자 전용
    """
    lookup_url_kwarg = 'category_id'

    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.all()
        else:
            category_id = self.kwargs['category_id']
            return Product.objects \
                .filter(category_id=category_id) \
                .prefetch_related('market') \
                .prefetch_related('category') \
                .all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return ProductListSerializer

