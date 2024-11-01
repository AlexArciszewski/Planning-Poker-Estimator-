from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from . models import Sprint


class SprintForm(ModelForm):
    """Creating class form for our sprint"""
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text="select users to add to the sprint"
    )
    class Meta:
        """metadata of our class"""

        model = Sprint
        fields = ['title', 'description', 'product_owner', 'created_by', 'users', 'chosen_users']
