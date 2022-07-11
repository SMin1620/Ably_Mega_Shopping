from django.urls import path

from product.views import (
    ProductListAPI,
)


product_list = ProductListAPI.as_view({
    'get': 'list',
})
product_detail = ProductListAPI.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    path('', product_list, name='Product List'),
    path('<int:product_id>', product_detail, name='Product Detail'),
]