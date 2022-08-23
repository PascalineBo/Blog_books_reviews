from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Username'}))
    password1 = forms.CharField(max_length=63, label='',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Mot de passe'}))
    password2 = forms.CharField(max_length=63, label='',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Confirmer le mot'
                                                                                 ' de passe'}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        role = forms.CharField(widget=forms.HiddenInput(), required=False)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur'}))
    password = forms.CharField(max_length=63, label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))
