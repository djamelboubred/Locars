from django import forms
"""
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserManager

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Nom d’utilisateur')
    password = forms.CharField(max_length=50, min_length=8, widget=forms.PasswordInput, label='Mot de passe')
"""
"""
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User  # Utilisez le modèle d'utilisateur personnalisé importé
        fields = ('email', 'username', 'password1', 'password2')

"""
