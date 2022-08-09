
from django.urls import path

from .views import *

urlpatterns = [
    path("user/", create_user),
    path("user/<int:id>", get_user),
    path('ShowItemCart/<int:cartId>', get_cart_item_by_cart_id),
    path('store/', cart_store),
    path('store/<int:userId>', get_store),
    path('login/', create_login),
    path('product/', product_list),
    path('product/find', search_product.as_view()),
    path('product/<int:id>', product_by_id),
    path('product/seller/<int:storeId>/', product_seller),
    path('cart/', cart_list),
    path('cart/seller/<int:userId>/', product_seller)






]
