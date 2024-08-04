from django.shortcuts import render, redirect

from . forms import TaskForm
from . models import Task
def tasks_main_page(request):

    return render(request, 'tasks/tasks_main_page.html')

def tasks_inside_page(request):

    return render(request, 'tasks/tasks_inside_page.html')


#
# def create_task(request):
#
#     form = TaskForm()
#
#     if request.method == 'POST':
#
#         form = TaskForm(request.POST)
#
#         if form.is_valid():
#
#             task = form.save(commit=False)
#
#             task.user = request.user
#
#             task.save()
#
#             return redirect('dashboard')
#
#     context = {'CreateTaskForm': form}
#
#     return render(request, 'tasks/create_task.html', context)

def my_tasks(request):
    form = TaskForm()

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)

            task.created_by = request.user

            task.save()

            return redirect('dashboard')

    tasks = Task.objects.all().filter(created_by=request.user)
    context = {'create_task_form': form, 'list_tasks': tasks}
    return render(request, 'tasks/my_tasks_page.html', context)

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
