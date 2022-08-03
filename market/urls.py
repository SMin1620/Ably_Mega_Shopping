from django.urls import path

from market.views import (
    MarketListDetailAPI,
    MarketProductListViewSet,
    MarketAdminProductListCreateViewSet
)


market_list = MarketListDetailAPI.as_view({
    'get': 'list'
})
market_detail = MarketListDetailAPI.as_view({
    'get': 'retrieve'
})

market_product_list = MarketProductListViewSet.as_view({
    'get': 'list'
})

market_admin_product_list = MarketAdminProductListCreateViewSet.as_view({
    'get': 'list',
    'post': 'create',
})


urlpatterns = [
    path('', market_list, name='market list'),
    path('<int:market_id>/', market_detail, name='market_detail'),
    path('<int:market_id>/product/', market_product_list),
    path('<int:market_id>/admin/product/', market_admin_product_list),
]


