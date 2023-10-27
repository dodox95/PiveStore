from django.contrib import admin
from django.urls import path, include
from . import views
from allauth.account.views import ConfirmEmailView, EmailVerificationSentView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="home"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("cart/", views.cart_view, name="cart"),
    path("checkout/", views.checkout_view, name="checkout"),
    path("accounts/", include("allauth.urls")),  # Add this lineaccount_confirm_email
    path("login-success/", views.login_success, name="login_success"),
    path("accounts/email/", views.change_email, name="change_email"),
]
