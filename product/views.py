from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from product.models import (
    Product,
    ProductReal,
    Category
)
from qna.models import Question
from qna.serializers import QuestionSerializer
from product.serializers import (
    CategorySerializer,
    ProductListSerializer,
    ProductDetailSerializer,
    ProductLikeSerializer,
)
from config.utils.pagination import LargeResultsSetPagination


# Create your views here.
class ProductListAPI(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    상품 리스트 조회 및 생성 뷰 - 사용자 전용
    """

    lookup_url_kwarg = 'product_id'
    queryset = Product.objects.all()
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        if self.action == 'list':
            search = self.request.GET.get('search', '')

            condition = Q()
            if search:
                condition.add(
                    Q(display_name__icontains=search) |
                    Q(market__name__icontains=search),
                    Q.OR
                )
            return Product.objects.filter(condition)
        elif self.action == 'retrieve':
            pk = self.kwargs['product_id']
            return Product.objects.filter(pk=pk)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'like':
            return ProductLikeSerializer
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
    pagination_class = LargeResultsSetPagination

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


class ProductQuestionListViewSet(mixins.ListModelMixin,
                                 viewsets.GenericViewSet):
    """
    상품별 질문 리스트 조회
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = LargeResultsSetPagination


class ProductRestoreViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    """
    삭제된 상품 리스트, 복구 뷰셋
    """
    lookup_url_kwarg = 'product_id'
    queryset = Product.objects.filter(is_deleted=True)
    serializer_class = ProductListSerializer

    @action(detail=True, methods=['post'])
    def restore(self, request, *args, **kwargs):
        """
        상품 복구
        """
        pk = self.kwargs['product_id']
        product = get_object_or_404(Product, pk=pk)
        product.retore()

        return Response(status=status.HTTP_200_OK)