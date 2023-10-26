from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="home"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("cart/", views.cart_view, name="cart"),
    path("checkout/", views.checkout_view, name="checkout"),
]
