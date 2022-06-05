from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .models import Account
from .forms import (
    RegistrationForm,
    AccountAuthenticationForm,
)

def register_user(request):
    """
    View to register new users to the website
    """
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("store-home")
    if request.POST:
        form = RegistrationForm(request.POST)
        redirect_url = request.POST.get("next") or "store-home"
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            messages.success(
                request,
                f"Thanks for registering,\
                    {request.user.first_name}! You are now logged in!",
            )
            return redirect(redirect_url)
        else:
            context["registration_form"] = form
    else:  # GET request
        form = RegistrationForm()
        context["registration_form"] = form
    return render(request, "accounts/register.html", context)


def logout_user(request):
    """
    View to log users out from the website
    """
    logout(request)
    messages.success(request, f"{'You have successfully logged out'}")
    return redirect("/")


def login_user(request):
    """
    View to log in previously registered users
    """
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("store-home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        redirect_url = request.POST.get("next") or "store-home"
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                messages.success(
                    request, f"Welcome back, {request.user.first_name}!"
                )
                return redirect(redirect_url)
        else:
            messages.error(request, f"{'Incorrect login details'}")
            context["login_form"] = form

    else:
        form = AccountAuthenticationForm()
        if request.POST.get("next"):
            messages.error(
                request, f"You must be logged in to access this page"
            )
        context["login_form"] = form
    return render(request, "accounts/login.html", context)
