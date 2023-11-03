from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from . import forms
from django.contrib.auth import login, authenticate, logout# import des fonctions login et authenticate
from django.contrib.auth.models import User
from django.contrib import messages

#from .forms import UserRegistrationForm
#from .models import CustomUserManager


def Home(request: HttpRequest):
    """
    The home function renders the home page of the LADN website.
    
    
    :param request: HttpRequest: Pass the request from the server to the function
    :return: The Home
    """
    return render(request, 'listings/Home.html')

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
        return redirect('Login')

    return render(request, 'listings/Register.html')

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            username = user.username
            return render(request, 'listings/Home.html', {'username': username})
        else:
            messages.error(request, 'Mauvaise authentification')
            return redirect('Login')
    return render(request, 'listings/Login.html')

def Logout(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté')
    return redirect('Home')



"""def Register_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Enregistrez l'utilisateur
            # Connectez automatiquement l'utilisateur après l'enregistrement
            login(request, user)
            return redirect("{% url 'Home' %}")  # Redirigez l'utilisateur vers une page de succès ou d'accueil

    else:
        form = UserRegistrationForm()

    return render(request, 'listings/Register.html', {'form': form})
"""
"""
def Register_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        phone_no = request.POST['phone_no']
    
        user = CustomUser(email = email, username = username, phone_no = phone_no)
        user.save()  # Enregistrez l'objet dans la base de données
        return redirect("{% url 'Home' %}")  # Redirigez vers une autre vue après l'enregistrement

    return render(request, 'listings/Register.html')


def Login_page(request):
    form = forms.LoginForm()
    message= ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'
    return render(request, 'listings/Login.html', context={'form': form, 'message': message})


"""
