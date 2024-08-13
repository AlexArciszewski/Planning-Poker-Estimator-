from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
# wrzucamy auth model z Django jest wbudowany

from django.contrib.auth import authenticate, login, logout
# importujemy też funkcje zawierające authentykację login i logout.

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# dekorator do ochrony widoków apliakcji aby nieutoryzowany user wszedł na dashboard


from django.db import transaction
from django.shortcuts import render

from .forms import UserForm, ProfileForm


from .models import User

# Create your views here.

def homepage(request):
    """widok strony głównej"""

    return render(request, 'users/index.html')

def register(request):
    """widok panelu rejestracji"""

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('my_login')

    context = {'RegistrationForm': form}

    return render(request, 'users/register.html', context)

def my_login(request):
    """widok panelu logowania"""

    form = LoginForm()
    # teraz sprawdzamy czy request jest postrequest
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        #  jesli post request to dane sa przeslane jako post request jesli formularz jest poprawny to łapiemy nazwe usera i hasło wpisano do formularza
        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)
        # sprawdzamy czy user jest autoryzowany authenticated

            if user is not None:

                auth.login(request, user)

                return redirect('dashboard')

        #Jeśli user jest poprawny i przeszedł ewaluację to go puszczamy na stronę dashboardu.

    context = {'LoginForm': form}

    return render(request, 'users/my_login.html', context)

@login_required(login_url='my_login')
def dashboard(request):
    """widok dashnoardu po logowaniu  tam nas prześle po poprawnym kologaniu"""

    return render(request, 'users/dashboard.html')




def user_logout(request):
    """ widok główny aplikacji po wylogowaniu widok robi redirect na stronę głowną"""

    auth.logout(request)

    return redirect("")


# def update_profile(request, user_id):
#
#     user = User.objects.get(pk=user_id)
#
#     user.profile.bio = ''
#
#     user.save()
#
#     return render(request, 'users/profile_management.html')


@login_required
@transaction.atomic
def update_profile(request):
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





