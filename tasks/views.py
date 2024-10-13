from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Min, Max
from .models import Task, TaskEstimation
from .forms import TaskEstimationForm, TaskForm
from sprints.models import Sprint


def tasks_main_page(request):
    """Task main page view """
    return render(request, 'tasks/tasks_main_page.html')


def tasks_inside_page(request):
    """Internal task page view """
    return render(request, 'tasks/tasks_inside_page.html')


def my_tasks(request):
    """View that shows the list of tasks"""
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('my_tasks_page')

    tasks = Task.objects.filter(created_by=request.user)
    paginator = Paginator(tasks, 3)
    page_number = request.GET.get('page')

    try:
        tasks_page = paginator.page(page_number)
    except PageNotAnInteger:
        tasks_page = paginator.page(1)
    except EmptyPage:
        tasks_page = paginator.page(paginator.num_pages)

    context = {
        'create_task_form': form,
        'list_tasks': tasks_page
    }

    return render(request, 'tasks/my_tasks_page.html', context)


def tasks_update(request, pk):
    """Task update view"""
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        else:
            return redirect('dashboard')

    context = {'UpdateTaskForm': form}
    return render(request, 'tasks/tasks_update_page.html', context)


def tasks_delete(request, pk):
    """Delete task view"""
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('my_tasks_page')

    return render(request, 'tasks/tasks_delete_page.html')


def task_detail(request, pk):
    """Task for detail view by its id"""
    task = get_object_or_404(Task, id=pk)
    context = {
        'task': task,
    }
    return render(request, 'tasks/task_detail_page.html', context)


# @login_required
# def estimate_task(request, task_id):
#     """Adding estimation to our tasks"""
#     task = get_object_or_404(Task, id=task_id)
#     if request.method == 'POST':
#         form = TaskEstimationForm(request.POST, task=task, user=request.user)
#         if form.is_valid():
#             estimation = form.save()
#
#             context = {
#                 'form': form,
#                 'task': task,
#                 'estimation': estimation,
#             }
#             return render(request, 'tasks/estimate_task.html', context)
#     else:
#         form = TaskEstimationForm(task=task, user=request.user)
#
#     context = {
#         'form': form,
#         'task': task,
#     }
#     return render(request, 'tasks/estimate_task.html', context)

# def estimate_task(request, pk: int, est_id: int):
#     """Task estimation View with possible estimation overwrite"""
#     task = get_object_or_404(Task, id=pk, est_id )
#     #czy jest już estymacja
#     try:
#         estimation = TaskEstimation.objects.get(task=task, estimated_by=request.user)
#     except TaskEstimation.DoesNotExist:
#         estimation = None
#
#     if request.method == 'POST':
#         form = TaskEstimationForm(request.POST, task=task, user=request.user)
#         if form.is_valid():
#             if estimation:
#                # jak jest już estymacja to nadpisuje
#                 estimation.estimation = form.cleaned_data['estimation']
#                 estimation.save()
#             else:
#                 # jak nie to nowa
#                 estimation = form.save(commit=False)
#                 estimation.task = task
#                 estimation.estimated_by = request.user
#                 estimation.save()
#             return redirect('task_detail_page', pk=pk)
#     else:
#         # Jak jest estym to do formularza
#         if estimation:
#             form = TaskEstimationForm(instance=estimation, task=task, user=request.user)
#         else:
#             form = TaskEstimationForm(task=task, user=request.user)
#     # Kontekst dla szablonu, aktualnej estymacja
#     context = {
#         'form': form,
#         'task': task,
#         'estimation': estimation,
#     }
#     return render(request, 'tasks/estimate_task.html', context)

def estimate_task(request, pk: int, est_id: int):
    """Task estimation View with possible estimation overwrite"""
    task = get_object_or_404(Task, id=pk)

    # try:
    estimation = TaskEstimation.objects.get(task=task, id=est_id, estimated_by=request.user)
    # except TaskEstimation.DoesNotExist:
    #     estimation = None

    if request.method == 'POST':
        form = TaskEstimationForm(request.POST, task=task, user=request.user)
        if form.is_valid():
            if estimation:

                estimation.estimation = form.cleaned_data['estimation']
                estimation.save()
            else:

                estimation = form.save(commit=False)
                estimation.task = task
                estimation.estimated_by = request.user
                estimation.save()
            return redirect('task_detail_page', pk=pk)
    else:

        if estimation:
            form = TaskEstimationForm(instance=estimation, task=task, user=request.user)
        else:
            form = TaskEstimationForm(task=task, user=request.user)

    context = {
        'form': form,
        'task': task,
        'estimation': estimation,
        'estimated_by': estimation.estimated_by if estimation else None,
    }

    return render(request, 'tasks/estimate_task.html', context)


def estimate_task_create(request, pk: int):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        form = TaskEstimationForm(request.POST, task=task, user=request.user)
        if form.is_valid():
            estimation = form.save(commit=False)
            estimation.user = request.user
            estimation.save()
            return redirect('task_detail_page', pk=pk)
    else:
        form = TaskEstimationForm(task=task, user=request.user)

    context = {
        'form': form,
    }
    return render(request, 'tasks/estimate-task-create.html', context)