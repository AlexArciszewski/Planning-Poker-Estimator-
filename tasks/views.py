

from . forms import TaskForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Min, Max
from .models import Task, TaskEstimation
from .forms import TaskEstimationForm



def tasks_main_page(request):

    return render(request, 'tasks/tasks_main_page.html')

def tasks_inside_page(request):

    return render(request, 'tasks/tasks_inside_page.html')



def my_tasks(request):

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('my_tasks_page')

    tasks = Task.objects.all().filter(created_by=request.user)

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




def tasks_update(request,pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

        else:

            return redirect('dashboard')

    context = {'UpdateTaskForm' : form}

    return render(request, 'tasks/tasks_update_page.html', context)

def tasks_delete(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == 'POST':

        task.delete()

        return redirect('my_tasks_page')

    return render(request, 'tasks/tasks_delete_page.html')


def task_detail(request, pk):
    task = get_object_or_404(Task, id=pk)
    context = {
        'task': task,
    }
    return render(request, 'tasks/task_detail_page.html', context)





# @login_required
def estimate_task(request, task_id):
    """Adding estimation to our tasks"""
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskEstimationForm(request.POST, task=task, user=request.user)
        if form.is_valid():
            estimation = form.save()

            # Sprawdź, czy wszystkie estymacje zostały podane
            if task.is_fully_estimated:
                estimations = task.estimations.all()
                min_estimation = estimations.aggregate(Min('estimation'))['estimation__min']
                max_estimation = estimations.aggregate(Max('estimation'))['estimation__max']

                # Jeśli są skrajne wartości, usuń wszystkie estymacje
                if min_estimation != max_estimation:
                    estimations.delete()
                    return redirect('estimate_task', task_id=task.id)

            return redirect('task_detail', pk=task.id)
    else:
        form = TaskEstimationForm(task=task, user=request.user)

    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'tasks/estimate_task.html', context)


