from django.shortcuts import render

# Create your views here.

# Vue de connexion des utilisateurs à notre application
def login(request):
    return render(request, 'users/login.html')


# Vue d'inscriptions des utilisateurs
def register(request):
    return render(request, 'users/register.html')
