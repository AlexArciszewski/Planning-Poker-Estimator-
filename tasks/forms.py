from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from . models import Task, TaskEstimation

class TaskForm(ModelForm):
    """Tworzymy klasę pod nasz modelform"""

    class Meta:
        """klasa ze specyfikacją formluarza"""
        model = Task
        fields = ['title', 'description', 'product_owner', 'user_story', 'sprint',]

class TaskEstimationForm(forms.ModelForm):
    """Formularz do estymacji """
    class Meta:
        """pola do modyfikacji"""
        model = TaskEstimation
        fields = ['estimation']

    def __init__(self, *args, **kwargs):
        self.task = kwargs.pop('task', None)
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    #     czy to zapewni poprawne działanie formularza opartego na args i kwargs?

    def clean(self):
        """validation method for pair user task if there is no one of them """
        cleaned_data = super().clean()
        if self.task and self.user:
            if not self.task.team_members.filter(id=self.user.id).exists():             #czy uztykownik jest członkiem zespołu przypisanego do zadania
                raise forms.ValidationError("Nie jesteś przypisany do tego zadania.")
            if TaskEstimation.objects.filter(task=self.task, estimated_by=self.user).exists():                  #czy doszło do estymacji
                raise forms.ValidationError("Już oszacowałeś to zadanie.")
        return cleaned_data

    def save(self, commit=True):
        """method for saving the form by creating an isntance ofTaskEstimation while not saving it"""
        instance = super().save(commit=False)
        instance.task = self.task
        instance.estimated_by = self.user
        if commit:
            instance.save()
        return instance
