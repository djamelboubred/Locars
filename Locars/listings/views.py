from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, JsonResponse
from . import forms
from django.contrib.auth import login, authenticate, logout # import des fonctions login et authenticate
from django.contrib.auth.decorators import login_required #import fonctions de gestions des authentifications pour les pages
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from .forms import UserForm, ProfilForm, AccountForm, EmailForm, CarForm, CarPlusForm, SearchCarsForm
from .models import User, Car
from django.utils import timezone 
from datetime import datetime
#from .utils import send_email_with_html_body
from .utils import Car_Id
from django.conf import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
#from .forms import UserRegistrationForm
#from .models import CustomUserManager


def Home(request: HttpRequest):
    if request.method == "POST":
        form = SearchCarsForm(request.POST)

        if form.is_valid():
            cars=Car.objects.all()

            marque = form.cleaned_data['marque']
            if marque != '':
                cars = cars.filter(marque=marque)
            model = form.cleaned_data.get('model','')
            if model != '':
                cars = cars.filter(model=model)
            city = form.cleaned_data.get('city','')
            if city != '':
                cars = cars.filter(city=city)
            country = form.cleaned_data.get('country','')
            if country != '':
                cars = cars.filter(country=country)
            
            print(marque)
            print(model)
            print(city)
            print(country)
            #print(car)
            return render(request, 'listings/Search.html', {'cars': cars})      

    return render(request, 'listings/Home.html')

def Search(request: HttpRequest):
    return render(request, 'listings/Search.html')

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

    return render(request, 'listings/Sign/Register.html')

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
    return render(request, 'listings/Sign/Login.html')

def Logout(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté')
    return redirect('Home')

@login_required
def Profile(request: HttpRequest):
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            # Enregistrez les modifications de l'utilisateur
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.profilePicture = form.cleaned_data['profilePicture']
            request.user.save()

            # Enregistrez le formulaire
            form.save()
            messages.success(request, 'Votre compte a été créé avec succès')
            return redirect('Profile')  # Redirigez l'utilisateur vers une autre page après la modification
    else:
        form = ProfilForm(instance=request.user)

    return render(request, 'listings/Account/Profile.html', {'form': form})


@login_required
def Account(request: HttpRequest):
    """
    The Profile function renders the Account page of the Locars website.

    - user can modify their informations and password? 
    
    :param request: HttpRequest: Pass the request from the server to the function
    :return: The Account
    """
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=request.user)
        if form.is_valid():
            # Enregistrez les modifications de l'utilisateur
            request.user.email = form.cleaned_data['email']
            request.user.country = form.cleaned_data['country']
            request.user.city = form.cleaned_data['city']
            request.user.street = form.cleaned_data['street']
            request.user.phone_no = form.cleaned_data['phone_no']
            request.user.save()
                       
             # Enregistrez le formulaire
            form.save()
            return redirect('Account')  # Redirigez l'utilisateur vers une autre page après la modification
    else:
        form = ProfilForm(instance=request.user)
    return render(request, 'listings/Account/Account.html')



"""

            # Création du message multipart (texte et HTML)
            message = MIMEMultipart("alternative")
            # Adresse e-mail du destinataire
            to_email = email
            # Création du message
            subject = 'Activation du compte'
            text_body = 'Bonjour bienvenue chez Locars'

            # Corps en HTML
            html_body = render_to_string('listings/EmailSend.html', {'username': username})  # Remplace avec tes données

            # Ajout des parties texte et HTML au message multipart
            message.attach(MIMEText(text_body, 'plain'))
            message.attach(MIMEText(html_body, 'html'))

            message = MIMEText(body)
            message['Subject'] = subject
            message['From'] = settings.EMAIL_HOST_USER
            message['To'] = to_email
            # Envoi de l'e-mail
            with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
                server.starttls()  # Utilisez cette ligne si EMAIL_USE_TLS est True
                server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                server.sendmail(settings.EMAIL_HOST_USER, [to_email], message.as_string())



"""
@login_required
def DeleteAccount(request: HttpRequest):
    if request.method == 'POST':
        # Supprimer l'utilisateur
        request.user.delete()
        # Déconnecter l'utilisateur
        logout(request)
        # Rediriger vers une page d'accueil ou une page appropriée
        return redirect('AccountDeleted')
    return render(request, 'listings/Account/DeleteAccount.html')

def AccountDeleted(request: HttpRequest):
    """
    Auto fresh page in 3 seconds redirect in home page
    """
    return render(request, 'listings/Account/AccountDelete.html')

@login_required
def DeleteCar(request, car_id):
    if request.method == 'POST':

        car = get_object_or_404(Car, Id_car=car_id, username=request.user)
        car.delete()
        return redirect('MyCars')
    return render(request, 'listings/Account/DeleteCar.html')

@login_required   
def Locarist(request: HttpRequest):
    """
    The Profile function renders the Locarist page of the Locars website.
    
    - this views register a user like a locarist, use formularies for register informations

    :param request: HttpRequest: Pass the request from the server to the function
    :return: The Locarist
    """
    if request.method == 'POST':
        form = CarForm(request.POST)


        # Vérifiez si le formulaire est valide
        if form.is_valid():
            Length_Car_Id = 8

            # Récupérez l'utilisateur actuellement connecté
            username = request.user

            # Créer et Vérifie que la clé primaire est unique
            ID = True
            while ID == True:
                Id_car = Car_Id(Length_Car_Id)
                if not Car.objects.filter(Id_car=Id_car).exists():
                    ID = False

            licence_plate = form.cleaned_data['licence_plate']

            marque = form.cleaned_data['marque']
            model = form.cleaned_data['model']
            year = form.cleaned_data['year']
            km = form.cleaned_data['km']

            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            street = form.cleaned_data['street']

            fuel = form.cleaned_data['fuel']

            car = Car.objects.create(username=username)


            car.Id_car = Id_car
            car.licence_plate = licence_plate
            car.username = username
            car.marque = marque
            car.model = model
            car.year = year
            car.km = km
            car.country = country
            car.city = city
            car.street = street
            car.fuel = fuel
            car.save()

            request.user.locarist = True
            request.user.save()

            ## Après avoir créé l'objet Car, récupérez son ID unique
            Id_car = car.Id_car

            ## Construisez l'URL de la vue de modification en utilisant l'ID de la voiture
            modification_url = reverse('LocaristPlus', kwargs={'car_id': Id_car})

            ## Redirigez l'utilisateur vers la vue de modification
            return redirect(modification_url)
        #return redirect('LocaristPlus')
        else:
            print(f"Form errors: {form.errors}")

    return render(request, 'listings/Account/Locarist.html')

@login_required
def LocaristPlus(request: HttpRequest, car_id):
    if request.method == 'POST':
        car = Car.objects.get(Id_car=car_id)
        form = CarPlusForm(request.POST)

        if form.is_valid():

            car.nb_door = form.cleaned_data['nb_door']
            car.geardbox = form.cleaned_data['geardbox']
            car.nb_place = form.cleaned_data['nb_place']
            car.Price = form.cleaned_data['Price']

            car.ProfileCarPicture = form.cleaned_data['ProfileCarPicture']
            car.Picture1 = form.cleaned_data['Picture1']
            car.Picture2 = form.cleaned_data['Picture2']
            car.Picture3 = form.cleaned_data['Picture3']

            car.save()

            return redirect('MyCars')
        # Récupérez l'objet Cars à modifier ou renvoyez une erreur 404 s'il n'existe pas
        #voiture = get_object_or_404(Cars, pk=voiture_id)
    return render(request, 'listings/Account/LocaristPlus.html')

@login_required
def MyCars(request: HttpRequest):
    """
    The Profile function renders the MyCars page of the Locars website.
    
    - show all cars of user
    
    :param request: HttpRequest: Pass the request from the server to the function
    :return: The MyCars
    """
    cars = Car.objects.filter(username=request.user)
    print(cars)
    print(request.user)
    return render(request, 'listings/Account/MyCars.html', {'cars': cars})

@login_required
def Favories(request: HttpRequest):
    """
    The Profile function renders the Favories page of the Locars website.
    
    - show favories of user

    :param request: HttpRequest: Pass the request from the server to the function
    :return: The Profile
    """
    return render(request, 'listings/Account/Favories.html')

@login_required
def Travel(request: HttpRequest):
    """
    The Profile function renders the Travel page of the Locars website.
    
    - show travel of user
    
    :param request: HttpRequest: Pass the request from the server to the function
    :return: The Profile
    """
    return render(request, 'listings/Account/Travel.html')

def Contact(request : HttpRequest):
    return render(request, 'listings/Contact.html')