from django.shortcuts import render

# Create your views here.

# Vue de connexion des utilisateurs à notre application
def index(request):
    return render(request, 'gestion_stock/index.html')