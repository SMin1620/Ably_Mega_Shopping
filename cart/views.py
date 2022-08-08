from django.shortcuts import get_object_or_404
from django.db import transaction

from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import action

from cart.models import CartItem
from cart.serializers import (
    CartSerializer,
    CartCreateSerializer,
    CartDetailUpdateDeleteSerializer
)


class CartUserViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    """
    유저별 장바구니 목록 조회
    """
    def get_queryset(self):
        return CartItem.objects \
            .filter(user=self.request.user) \
            .prefetch_related('product_real') \
            .all()

    def get_serializer_class(self):
        return CartSerializer


class CartCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    장바구니 생성
    """
    queryset = CartItem.objects.all()
    serializer_class = CartCreateSerializer

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartDetailUpdateDeleteViewSet(mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    viewsets.GenericViewSet):
    """
    장바구니 상세 조회, 수정, 삭제
    """
    lookup_url_kwarg = 'cart_id'
    queryset = CartItem.objects.all()
    serializer_class = CartDetailUpdateDeleteSerializer

    def partial_update(self, request, *args, **kwargs):
        """
        본인 마켓의 상품 부분 수정
        """
        kwargs['partial'] = True

        return self.update(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def up(self, request, *args, **kwargs):
        """
        장바구니 아이템 개수 + 1
        """
        pk = self.kwargs['cart_id']
        cart_item = get_object_or_404(CartItem, pk=pk)

        if cart_item.quantity < 100:
            cart_item.quantity += 1
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def down(self, request, *args, **kwargs):
        """
        장바구니 아이템 개수 - 1
        """
        pk = self.kwargs['cart_id']
        cart_item = get_object_or_404(CartItem, pk=pk)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)
