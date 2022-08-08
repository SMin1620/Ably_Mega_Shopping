from django.urls import path

from cart.views import (
    CartUserViewSet,
    CartDetailUpdateDeleteViewSet
)


cart_user = CartUserViewSet.as_view({
    'get': 'list'
})

cart_detail_update_delete = CartDetailUpdateDeleteViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

cart_up = CartDetailUpdateDeleteViewSet.as_view({
    'post': 'up'
})

cart_down = CartDetailUpdateDeleteViewSet.as_view({
    'post': 'down'
})


urlpatterns = [
    path('user/<int:user_id>/', cart_user),
    path('<int:cart_id>/', cart_detail_update_delete),
    path('<int:cart_id>/up/', cart_up),
    path('<int:cart_id>/down/', cart_down),
]