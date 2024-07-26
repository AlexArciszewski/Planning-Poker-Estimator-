from django.forms import ModelForm

from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput

from . models import Task


class TaskForm(ModelForm):
    """Tworzymy klasę pod nasz modelform"""

    class Meta:
        model = Task
        fields = '__all__'
