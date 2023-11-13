from django import forms
from .models import User, Cars, Car

class UserForm(forms.ModelForm):
    class Meta:
        
        model = User
        
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_no', 'password']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['licence_plate','marque', 'model', 'year', 'fuel','km', 'country', 'city', 'street', 'username']

class CarTestForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['licences_plate', 'marque', 'model', 'year','km', 'country', 'city', 'street', 'fuel']
        exclude = ['username']

class CarPlusForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['nb_door', 'geardbox', 'profilePicture']

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

