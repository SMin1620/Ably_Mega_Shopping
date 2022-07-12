from rest_framework import mixins, viewsets

from market.serializers import (
    MarketListSerializer,
    MarketDetailSerializer,
)
from market.models import Market


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

