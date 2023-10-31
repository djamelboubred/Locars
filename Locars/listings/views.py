from django.shortcuts import render
from django.http import HttpRequest, JsonResponse




def Home(request: HttpRequest):
    """
    The home function renders the home page of the LADN website.
    
    
    :param request: HttpRequest: Pass the request from the server to the function
    :return: The Home
    """
    return render(request, 'listings/Home.html')

def Login(request: HttpRequest):

    return render(request, 'listings/Login.html')