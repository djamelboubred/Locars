from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from . import forms
from django.contrib.auth import login, authenticate # import des fonctions login et authenticate


def Home(request: HttpRequest):
    """
    The home function renders the home page of the LADN website.
    
    
    :param request: HttpRequest: Pass the request from the server to the function
    :return: The Home
    """
    return render(request, 'listings/Home.html')

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
