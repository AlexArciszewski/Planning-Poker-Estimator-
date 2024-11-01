from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render
from .forms import UserForm, ProfileForm
from .models import User


def homepage(request: HttpRequest) -> HttpResponse:
    """View for the homepage."""
    return render(request, 'users/index.html')


def register(request: HttpRequest) -> HttpResponse:
    """View for the registration panel."""
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_login')

    context = {'RegistrationForm': form}
    return render(request, 'users/register.html', context)


def my_login(request: HttpRequest) -> HttpResponse:
    """Login page view."""
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = {'LoginForm': form}
    return render(request, 'users/my_login.html', context)


@login_required(login_url='my_login')
def dashboard(request: HttpRequest) -> HttpResponse:
    """Dashboard view after login; redirects here upon successful login."""

    return render(request, 'users/dashboard.html')


def user_logout(request: HttpRequest) -> HttpResponse:
    """ View for logging out the user; redirects to the homepage after logout."""

    auth.logout(request)
    return redirect("")


@login_required
@transaction.atomic
def update_profile(request: HttpRequest) -> HttpResponse:
    """View used for the profile update. """

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })





