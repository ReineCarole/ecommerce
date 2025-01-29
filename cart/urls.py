from django.urls import path
from .views import CartList, CartItemList, CartItemDetail

urlpatterns = [
    path('carts/', CartList.as_view(), name='cart-list'),
    path('cart-items/', CartItemList.as_view(), name='cart-item-list'),
    path('cart-items/<int:pk>/', CartItemDetail.as_view(), name='cart-item-detail'),
]
