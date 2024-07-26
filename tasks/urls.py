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
    path('tasks_main_page', views.tasks_main_page, name="tasks_main_page"),
    path('tasks_inside_page', views.tasks_inside_page, name="tasks_inside_page"),
    path('create_task', views.create_task, name="create_task")
]
