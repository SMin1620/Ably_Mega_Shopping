from rest_framework import mixins, viewsets

from market.serializers import (
    MarketListSerializer,
    MarketDetailSerializer,
    MarketProductListSerializer
)
from market.models import Market
from product.models import Product, ProductReal


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
    lookup_url_kwarg = 'market_id'

    def get_queryset(self):
        market_id = self.kwargs['market_id']

        return Product.objects \
            .filter(market_id=market_id) \
            .prefetch_related('market') \
            .prefetch_related('category') \
            .all()

    def get_serializer_class(self):
        return MarketProductListSerializer




