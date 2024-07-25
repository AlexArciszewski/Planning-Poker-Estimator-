from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# defaultowy formularz do budowania modeli


from django.contrib.auth.models import User

from django.forms.widgets import PasswordInput, TextInput

from django import forms

class CreateUserForm(UserCreationForm):
    ''' tworzymy model przez klasę CreateUserForm(UsercreationForm) dziedziczymy po pierwszym imporcie.'''


    class Meta:
        '''   Korzystamy tutaj zagnieżdżonej klasy Meta
              Doprecyzujemy model i tu bierzemy usera bierzemy pola i listę z atrybutami do uzupełnienia aby mozna było wygenerowac usera'''
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    '''Tworzę klase gdzie przekazuję klase bazową authentication form'''

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

    # Textinput do wpisania nazwy usera passwordinput do wpisania hasła z kropkami zamaist liter