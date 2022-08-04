from django.shortcuts import get_object_or_404

from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

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
            return Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        else:
            return ProductDetailSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, *args, **kwargs):
        """
        좋아요 기능 (찜하기)
        """
        pk = kwargs['product_id']
        user = request.user
        product = get_object_or_404(Product, pk=pk)

        if product.product_like_user.filter(pk=user.id).exists():
            product.product_like_user.remove(user.id)
        else:
            product.product_like_user.add(user.id)

        return Response(status=status.HTTP_200_OK)


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

