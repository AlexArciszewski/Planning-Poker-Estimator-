from django.forms import ModelForm

from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput

from . models import Sprint


class SprintForm(ModelForm):
    """Tworzymy klasę pod nasz modelform"""

    class Meta:
        """metadane dla naszej klasy zdefiniowanie klasy,którą chcemy użyć"""

        model = Sprint
        fields = ['sprint_id', 'sprint_title', 'sprint_info', 'po_name', ]
        exclude = ['user',]