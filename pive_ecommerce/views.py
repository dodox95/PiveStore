from allauth.account.views import SignupView
from allauth.account.forms import SignupForm
from django.shortcuts import render, redirect
from django.contrib import messages
from allauth.account.forms import LoginForm
from django.http import JsonResponse


def index(request):
    return render(request, "index.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST, request=request)
        if form.is_valid():
            # Log the user in
            form.login(request)
            messages.success(request, "Logged in successfully!")
            return redirect(
                "login_success"
            )  # Redirect to a view where you can show the success message and then redirect
        else:
            print(form.errors)  # This will print the form errors when you try to log in
            messages.error(request, "Invalid login credentials.")
    else:
        form = LoginForm()

    return render(request, "account/login.html", {"form": form})


def login_success(request):
    return JsonResponse({"status": "success", "message": "Logged in successfully!"})


def register_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, "registered")
            return redirect("confirm_email")  # Zmienione przekierowanie
    else:
        form = SignupForm()

    return render(request, "register.html", {"form": form})


def cart_view(request):
    return render(request, "cart.html")


def checkout_view(request):
    return render(request, "checkout.html")


def change_email(request):
    return render(request, "account/email_change.html")
