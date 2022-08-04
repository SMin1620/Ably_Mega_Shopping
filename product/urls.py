from django.urls import path

from product.views import (
    ProductListAPI,
    CategoryProductListViewSet
)


product_list = ProductListAPI.as_view({
    'get': 'list',
})
product_detail = ProductListAPI.as_view({
    'get': 'retrieve'
})

category_list = CategoryProductListViewSet.as_view({
    'get': 'list'
})

category_product_list = CategoryProductListViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    path('', product_list, name='Product List'),
    path('<int:product_id>', product_detail, name='Product Detail'),
    path('category/', category_list),
    path('category/<int:category_id>/', category_product_list),
]