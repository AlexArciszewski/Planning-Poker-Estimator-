from django.shortcuts import render, redirect
from . forms import SprintForm
from . models import Sprint
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

def sprints_main_page(request):
    """View of the main sprint page"""

    return render(request, 'sprints/sprints_main_page.html')


def sprints_inside_page(request):
    """View of inside sprint page """

    return render(request, 'sprints/sprints_inside_page.html')


def create_sprint(request):
    """View for adding a sprint"""

    form2 = SprintForm()

    if request.method == 'POST':
        form2 = SprintForm(request.POST)
        if form2.is_valid():
            sprint = form2.save(commit=False)
            sprint.user = request.user
            sprint.save()
            form2.save_m2m()
            return redirect('sprints_main_page')

    context = {'CreateSprintForm': form2}

    return render(request, 'sprints/create_sprint.html', context)


def my_sprints(request):
    """View for showing the sprints"""

    form2 = SprintForm()

    if request.method == 'POST':
        form2 = SprintForm(request.POST)
        if form2.is_valid():
            sprint = form2.save(commit=False)
            sprint.created_by = request.user
            sprint.save()
            form2.save_m2m()
            return redirect('dashboard')

    sprints = Sprint.objects.filter(Q(created_by=request.user) | Q(users=request.user)
                                    ).distinct()
    # sprints = Sprint.objects.filter(created_by=request.user)
    for sprint in sprints:
        print(f"Sprint: {sprint.title} has users: {sprint.users.all()}")  # Debug mója wersja wszystkei sprinty usera wyciagnalem i d..a


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
    """updating sprint view"""

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
    """View for removing the sprint"""

    sprints = Sprint.objects.get(id=pk)

    if request.method == 'POST':
        sprints.delete()
        return redirect('my_sprints')

    return render(request, 'sprints/sprints_delete.html')






