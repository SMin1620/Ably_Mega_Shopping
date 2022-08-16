from django.db import transaction

from rest_framework import mixins, viewsets
from rest_framework.decorators import action

from market.serializers import (
    MarketListSerializer,
    MarketDetailSerializer,
    MarketProductListSerializer,
    MarketAdminDetailSerializer,
    MarketAdminProductListCreateSerializer,
    MarketAdminUpdateDeleteSerializer,
    MarketAdminProductRealListCreateSerializer
)
from market.models import Market
from product.models import Product, ProductReal
from config.utils.pagination import LargeResultsSetPagination


# Create your views here.
class MarketListDetailAPI(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    마켓 목록 조회 뷰 - 사용자 전용
    """
    lookup_url_kwarg = 'market_id'

    def get_queryset(self):
        return Market.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return MarketListSerializer
        else:
            return MarketDetailSerializer


class MarketProductListViewSet(mixins.ListModelMixin,
                               viewsets.GenericViewSet):
    """
    마켓별 상품 목록 조회 뷰셋 - 사용자 전용
    """
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        market_id = self.kwargs['market_id']

        return Product.objects \
            .filter(market_id=market_id) \
            .prefetch_related('market') \
            .prefetch_related('category') \
            .all()

    def get_serializer_class(self):
        return MarketProductListSerializer


class MarketProductDetailUpdateDeleteViewSet(mixins.RetrieveModelMixin,
                                             mixins.UpdateModelMixin,
                                             mixins.DestroyModelMixin,
                                             viewsets.GenericViewSet):
    """
    마켓별 상품 상세 조회
    수정
    삭제
    마켓 관리자 전용
    """
    lookup_url_kwarg = 'product_id'

    def get_queryset(self):
        market_id = self.kwargs['market_id']

        return Product.objects \
            .filter(market_id=market_id) \
            .prefetch_related('market') \
            .prefetch_related('product_real') \
            .all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MarketAdminDetailSerializer
        else:
            return MarketAdminUpdateDeleteSerializer

    def partial_update(self, request, *args, **kwargs):
        """
        본인 마켓의 상품 부분 수정
        """
        kwargs['partial'] = True

        return self.update(request, *args, **kwargs)


class MarketAdminProductRealListCreateViewSet(mixins.ListModelMixin,
                                              mixins.CreateModelMixin,
                                              viewsets.GenericViewSet):
    """
    본인 마켓의 상품 옵션 목록 조회
    생성
    마켓 관리자 전용
    """
    lookup_url_kwarg = 'product_id'

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        market_id = self.kwargs['market_id']

        return ProductReal.objects \
            .filter(product__market_id=market_id, product=product_id) \
            .all()

    def get_serializer_class(self):
        return MarketAdminProductRealListCreateSerializer


class MarketAdminProductListCreateViewSet(mixins.ListModelMixin,
                                          mixins.CreateModelMixin,
                                          viewsets.GenericViewSet):
    """
    마켓별 상품 목록 조회, 생성 뷰셋 - 마켓 관리자용
    """

    def get_queryset(self):
        market_id = self.kwargs['market_id']

        return Product.objects \
            .filter(market_id=market_id) \
            .prefetch_related('market') \
            .prefetch_related('category') \
            .all()

    def get_serializer_class(self):
        return MarketAdminProductListCreateSerializer

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(market_id=self.kwargs['market_id'])




