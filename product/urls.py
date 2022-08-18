from django.urls import path

from product.views import (
    ProductListAPI,
    CategoryProductListViewSet,
    ProductQuestionListViewSet,
    ProductRestoreViewSet,
)
from review.views import ReviewListCreateViewSet


product_list = ProductListAPI.as_view({
    'get': 'list',
})
product_detail = ProductListAPI.as_view({
    'get': 'retrieve',
})

product_like = ProductListAPI.as_view({
    'post': 'like'
})

category_list = CategoryProductListViewSet.as_view({
    'get': 'list'
})

category_product_list = CategoryProductListViewSet.as_view({
    'get': 'retrieve'
})

product_question_list = ProductQuestionListViewSet.as_view({
    'get': 'list'
})

product_review = ReviewListCreateViewSet.as_view({
    'get': 'list'
})

product_delete_list = ProductRestoreViewSet.as_view({
    'get': 'list'
})

product_delete_restore = ProductRestoreViewSet.as_view({
    'get': 'retrieve',
    'patch': 'restore'
})


urlpatterns = [
    path('', product_list, name='Product List'),
    path('<int:product_id>/', product_detail, name='Product Detail'),
    path('<int:product_id>/like/', product_like, name='Product Like'),
    path('category/', category_list),
    path('category/<int:category_id>/', category_product_list),
    path('<int:product_id>/question/', product_question_list),
    path('<int:product_id>/review/', product_review),
    path('delete/', product_delete_list),
    path('delete/<int:product_id>/', product_delete_restore),
]