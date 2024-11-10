"""
URL configuration for ppoker_fin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('tasks_main_page', views.tasks_main_page, name="tasks_main_page"), # tasks

    path('my_tasks_page', views.my_tasks, name="my_tasks_page"), # tasks/my
    path('tasks_update_page/<str:pk>', views.tasks_update, name="tasks_update_page"), # tasks/<str:pk>/update
    path('tasks_delete_page/<str:pk>', views.tasks_delete, name="tasks_delete_page"), # tasks/<str:pk>/delete
    path('task_detail_page/<str:pk>', views.task_detail, name="task_detail_page"), # tasks/<str:pk>/
    path('task/<str:pk>/estimate/<str:est_id>', views.estimate_task, name='estimate_task'), # tasks/<str:pk>/estimates/<str:est_id>

    path('estimate-task-create/<int:pk>', views.estimate_task_create, name="estimate-task-create"), # tasks/<int:pk>/estimates

]
