from django import forms
from .models import User, Car

class UserForm(forms.ModelForm):
    class Meta:
        
        model = User
        
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_no', 'password']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['licence_plate', 'marque', 'model', 'year','km', 'country', 'city', 'street', 'fuel']
        exclude = ['username', 'Id_car']

class CarPlusForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['nb_door', 'nb_place', 'geardbox', 'Price', 'ProfileCarPicture', 'Picture1', 'Picture2', 'Picture3']

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

class SearchCarsForm(forms.Form):
    marque = forms.CharField(max_length=20, required=False)
    model = forms.CharField(max_length=20, required=False)
    city = forms.CharField(max_length=58, required=False)
    country = forms.CharField(max_length=42, required=False)
