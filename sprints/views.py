from django.shortcuts import render, redirect

from . forms import SprintForm
from . models import Sprint

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def sprints_main_page(request):

    return render(request, 'sprints/sprints_main_page.html')

def sprints_inside_page(request):

    return render(request, 'sprints/sprints_inside_page.html')


def create_sprint(request):

    form2 = SprintForm()

    if request.method == 'POST':

        form2 = SprintForm(request.POST)

        if form2.is_valid():

            sprint = form2.save(commit=False)

            sprint.user = request.user

            sprint.save()

            return redirect('sprints_main_page')

    context = {'CreateSprintForm': form2}

    return render(request, 'sprints/create_sprint.html', context)

# def my_sprints(request):
#
#     form2 = SprintForm()
#
#     if request.method == 'POST':
#
#         form2 = SprintForm(request.POST)
#
#         if form2.is_valid():
#             sprint = form2.save(commit=False)
#
#             sprint.created_by = request.user
#
#             sprint.save()
#
#             return redirect('dashboard')
#
#     sprints = Sprint.objects.all().filter(created_by=request.user)
#
#
#     context = {'create_sprint_form': form2, 'list_sprints' : sprints}
#
#     return render(request, 'sprints/my_sprints2.html', context)
def my_sprints(request):
    form2 = SprintForm()

    if request.method == 'POST':
        form2 = SprintForm(request.POST)
        if form2.is_valid():
            sprint = form2.save(commit=False)
            sprint.created_by = request.user
            sprint.save()
            return redirect('dashboard')

    # Pobieramy wszystkie sprinty stworzone przez użytkownika
    sprints = Sprint.objects.all().filter(created_by=request.user)

    # Ustawiamy paginację na 10 elementów na stronę
    paginator = Paginator(sprints, 3)  # 10 sprintów na stronę
    page_number = request.GET.get('page')

    try:
        sprints_page = paginator.page(page_number)
    except PageNotAnInteger:
        # Jeżeli page_number nie jest liczbą całkowitą, wyświetlamy pierwszą stronę
        sprints_page = paginator.page(1)
    except EmptyPage:
        # Jeżeli page_number jest poza zakresem (np. za duża liczba), wyświetlamy ostatnią stronę
        sprints_page = paginator.page(paginator.num_pages)

    context = {
        'create_sprint_form': form2,
        'list_sprints': sprints_page
    }

    return render(request, 'sprints/my_sprints.html', context)



def sprints_update(request, pk):

    sprints = Sprint.objects.get(id=pk)

    form2 = SprintForm(instance=sprints)

    if request.method == 'POST':

        form2 = SprintForm(request.POST, instance=sprints)

        if form2.is_valid():

            form2.save()

            return redirect('dashboard')

    context = {'UpdateSprintForm': form2}

    return render(request, 'sprints/sprints_update.html', context)


def delete_sprints(request, pk):

    sprints = Sprint.objects.get(id=pk)

    # return redirect('dashboard')

    if request.method == 'POST':

        sprints.delete()

        return redirect('my_sprints')


    return render(request, 'sprints/sprints_delete.html')







    # sprint = Sprint.objects.all().filter(created_by=request.user)
    #
    #
    # return render(request, 'sprints/my_sprints2.html')




# from . forms import CreateUserForm, LoginForm
#
# from django.contrib.auth.models import auth
# # wrzucamy auth model z Django jest wbudowany
#
# from django.contrib.auth import authenticate, login, logout
# # importujemy też funkcje zawierające authentykację login i logout.
#
#
# from django.contrib.auth.decorators import login_required
# # dekorator do ochrony widoków apliakcji aby nieutoryzowany user wszedł na dashboard
#
#
# # Create your views here.
#
# def homepage(request):
#     """widok strony głównej"""
#
#     return render(request, 'users/index.html')
#
# def register(request):
#     """widok panelu rejestracji"""
#
#     form = CreateUserForm()
#
#     if request.method == 'POST':
#
#         form = CreateUserForm(request.POST)
#
#         if form.is_valid():
#
#             form.save()
#
#             return redirect('my_login')
#
#     context = {'RegistrationForm': form}
#
#     return render(request, 'users/register.html', context)
#
# def my_login(request):
#     """widok panelu logowania"""
#
#     form = LoginForm()
#     # teraz sprawdzamy czy request jest postrequest
#     if request.method == 'POST':
#         form = LoginForm(request, data=request.POST)
#
#         #  jesli post request to dane sa przeslane jako post request jesli formularz jest poprawny to łapiemy nazwe usera i hasło wpisano do formularza
#         if form.is_valid():
#
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#
#             user = authenticate(request,username=username,password=password)
#         # sprawdzamy czy user jest autoryzowany authenticated
#
#             if user is not None:
#
#                 auth.login(request, user)
#
#                 return redirect('dashboard')
#
#         #Jeśli user jest poprawny i przeszedł ewaluację to go puszczamy na stronę dashboardu.
#
#     context = {'LoginForm': form}
#
#     return render(request, 'users/my_login.html', context)
#
# @login_required(login_url='my_login')
# def dashboard(request):
#     """widok dashnoardu po logowaniu  tam nas prześle po poprawnym kologaniu"""
#
#     return render(request, 'users/dashboard.html')
#
#
#
#
# def user_logout(request):
#     """ widok główny aplikacji po wylogowaniu widok robi redirect na stronę głowną"""
#
#     auth.logout(request)
#
#     return redirect("")
#
#
# #
