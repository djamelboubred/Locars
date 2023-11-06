from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from . import forms
from django.contrib.auth import login, authenticate, logout # import des fonctions login et authenticate
from django.contrib.auth.decorators import login_required #import fonctions de gestions des authentifications pour les pages
from django.contrib.auth.models import User
from django.contrib import messages
from Locars import settings
from django.core.mail import send_mail
from .forms import UserForm
from .models import User, Car
from django.utils import timezone

#from .forms import UserRegistrationForm
#from .models import CustomUserManager


def Home(request: HttpRequest):
    """
    The home function renders the home page of the Locars website.
    
    
    :param request: HttpRequest: Pass the request from the server to the function
    :return: The Home
    """
    return render(request, 'listings/Home.html')


def Register(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            # Vérifiez si les mots de passe correspondent
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_no = form.cleaned_data['phone_no']
            # Créez l'objet utilisateur
            user = User.objects.create_user(username=username, email=email, password=form.cleaned_data['password'])
            user.first_name = first_name
            user.last_name = last_name
            user.phone_no = phone_no
            user.date_creation = timezone.now()
            user.save()
            
            login(request, user)  # Connectez l'utilisateur immédiatement après la création du compte
            messages.success(request, 'Votre compte a été créé avec succès')
            return redirect('Login')

        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')

    return render(request, 'listings/Register.html')

"""
def Register(request):

    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        if User.objects.filter(username=username):
            messages.error(request, "Ce nom d'utilisateur est déjà pris")
            return redirect('Register')

        if User.objects.filter(email=email):
            messages.error(request, "Cet email à déjà un comptes")
            return redirect('Register')

        if not username.isalnum():
            messages.error(request, "Le nom d'utilisateur doit être alphanuméric")
            return redirect('Register')

        if password != password1:
            messages.error(request, "Les deux mot de passe ne coincide pas !")
            return redirect('Register')

        my_user = User.objects.create_user(username, email, password)
        my_user.first_name = firstname
        my_user.last_name = lastname
        my_user.phone_no = phone_no
        my_user.save()
        messages.success(request, 'Votre compte à été créer avec succès')
"""        
"""
        Send email after create User for the first time
        
        subject = "Bienvenue sur Locars"
        message = "Bienvenue" + my_user.first_name + " " + my_user.last_name + "\n Nous sommesheureux de vous compter aprmis nous \n\n\n Merci\n"
        from_email = settings.EMAIL_HOST_USER
        to_list = [my_user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)
"""
"""
        return redirect('Login')

    return render(request, 'listings/Register.html')
"""
def Login(request):
    if request.user.is_authenticated:
        return redirect('Profile')
    else:
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                username = user.username
                return render(request, 'listings/Profile.html', {'username': username})
            else:
                messages.error(request, 'Mauvaise authentification')
                return redirect('Login')
    return render(request, 'listings/Login.html')

def Logout(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté')
    return redirect('Home')

@login_required
def Profile(request: HttpRequest):
    """
    The Profile function renders the Profile page of the Locars website.
    
    - shows informations

    :param request: HttpRequest: Pass the request from the server to the function
    :return: The Profile
    """
    return render(request, 'listings/Profile.html')

@login_required
def Account(request: HttpRequest):
    """
    The Profile function renders the Account page of the Locars website.

    - user can modify their informations and password? 
    
    :param request: HttpRequest: Pass the request from the server to the function
    :return: The Account
    """
    return render(request, 'listings/Account.html')

def Locarist(request: HttpRequest):
    """
    The Profile function renders the Locarist page of the Locars website.
    
    - this views register a user like a locarist, use formularies for register informations

    :param request: HttpRequest: Pass the request from the server to the function
    :return: The Locarist
    """
    return render(request, 'listings/Locarist.html')

@login_required
def Favories(request: HttpRequest):
    """
    The Profile function renders the Favories page of the Locars website.
    
    - show favories of user

    :param request: HttpRequest: Pass the request from the server to the function
    :return: The Profile
    """
    return render(request, 'listings/Favories.html')

@login_required
def Travel(request: HttpRequest):
    """
    The Profile function renders the Travel page of the Locars website.
    
    - show travel of user
    
    :param request: HttpRequest: Pass the request from the server to the function
    :return: The Profile
    """
    return render(request, 'listings/Travel.html')

@login_required
def MyCars(request: HttpRequest):
    """
    The Profile function renders the MyCars page of the Locars website.
    
    - show all cars of user
    
    :param request: HttpRequest: Pass the request from the server to the function
    :return: The MyCars
    """
    return render(request, 'listings/MyCars.html')