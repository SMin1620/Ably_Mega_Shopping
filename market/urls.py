from django.urls import path

from market.views import (
    MarketListDetailAPI,
)


market_list = MarketListDetailAPI.as_view({
    'get': 'list'
})
market_detail = MarketListDetailAPI.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    path('', market_list, name='market list'),
    path('<int:market_id>/', market_detail, name='market_detail'),
]


