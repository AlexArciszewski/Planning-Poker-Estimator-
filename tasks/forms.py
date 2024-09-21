from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from . models import Task, TaskEstimation


class TaskForm(ModelForm):
    """bulidning task form"""
    class Meta:
        """Task spec"""
        model = Task
        fields = ['title', 'description', 'product_owner', 'user_story', 'sprint',]


class TaskEstimationForm(forms.ModelForm):
    """Building estimation form """
    class Meta:
        """Fields for estiamtion"""
        model = TaskEstimation
        fields = ['estimation']

    def __init__(self, *args, **kwargs):
        self.task = kwargs.pop('task', None)
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        #     czy to zapewni poprawne działanie formularza opartego na args i kwargs?

    def save(self, commit=True):
        estimation = super().save(commit=False)
        estimation.task = self.task  # Ustawienie pola task
        if commit:
            estimation.save()
        return estimation