from django import forms
from .models import User, Car

class UserForm(forms.ModelForm):
    class Meta:
        
        model = User
        
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_no', 'password']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['marque', 'model', 'year', 'fuel']

class ProfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profilePicture', 'first_name', 'last_name']

class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'country', 'city', 'street', 'phone_no']


class EmailForm(forms.Form):
    to_email = forms.EmailField(label='Destinataire')

