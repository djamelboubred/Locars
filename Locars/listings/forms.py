from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Nom d’utilisateur')
    password = forms.CharField(max_length=50, min_length=8, widget=forms.PasswordInput, label='Mot de passe')