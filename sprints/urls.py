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
    path('sprints_main_page', views.sprints_main_page, name="sprints_main_page"),
    path('sprints_inside_page', views.sprints_inside_page, name="sprints_inside_page"),
    path('create_sprint', views.create_sprint, name="create_sprint"),
    path('my_sprints', views.my_sprints, name="my_sprints"),
    path('sprints_update/<str:pk>', views.sprints_update, name="sprints_update"),
    path('sprints_delete/<str:pk>', views.delete_sprints, name="sprints_delete")

]
