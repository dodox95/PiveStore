from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def login_view(request):
    return render(request, "login.html")


def register_view(request):
    return render(request, "register.html")


def cart_view(request):
    return render(request, "cart.html")


def checkout_view(request):
    return render(request, "checkout.html")
