from unicodedata import name
from django.urls import path
from listings import views


urlpatterns = [
    path('', views.Home, name='Home'),
    path('search/', views.Search, name='Search'),
    path('register/', views.Register, name='Register'),
    path('login/', views.Login, name='Login'),
    path('logout/', views.Logout, name='Logout'),
    path('profile/', views.Profile, name='Profile'),
    path('account/', views.Account, name='Account'),
    path('locarist/', views.Locarist, name='Locarist'),
    path('favories/', views.Favories, name='Favories'),
    path('travel/', views.Travel, name='Travel'),
    path('mycars/', views.MyCars, name='MyCars'),
    path('deleteAccount/', views.DeleteAccount, name='DeleteAccount'),
    path('accountDeleted/', views.AccountDeleted, name='AccountDeleted'),
    path('deleteCar/<str:car_id>/', views.DeleteCar, name='DeleteCar'),
    path('locaristPlus/<str:car_id>/', views.LocaristPlus, name='LocaristPlus'),
    path('contact/', views.Contact, name='Contact'),
]