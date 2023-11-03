from unicodedata import name
from django.urls import path
from listings import views


urlpatterns = [
    path('', views.Home, name='Home'),
    path('register/', views.Register, name='Register'),
    path('login/', views.Login, name='Login'),
    path('logout/', views.Logout, name='Logout'),
]