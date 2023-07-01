from django.urls import path
from . import views

urlpatterns=[
    path('',views.store,name="storepage"),
    path('cart/',views.cart,name="cartpage"),
    path('account/',views.account,name="accountpage"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('checkout/',views.checkout,name="checkoutpage"),
    path('signuppage/',views.signuppage,name="signuppage"),
    path('searchpage/',views.searchpage,name="searchpage"),
    path('productpage/<str:id>/',views.productpage,name="productpage"),
]