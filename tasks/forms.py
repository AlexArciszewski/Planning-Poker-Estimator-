from django.forms import ModelForm

from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput

from . models import Task


class TaskForm(ModelForm):
    """Tworzymy klasę pod nasz modelform"""

    class Meta:
        model = Task
        fields = ['task_id', 'task_title', 'task_info', 'po_name', 'task_owner', 'user_story',]
        exclude = ['user',]
