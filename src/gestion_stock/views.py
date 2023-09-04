from django.shortcuts import render
from users.models import Utilisateur

from django.contrib.auth.decorators import login_required
# Create your views here.

# Vue de connexion des utilisateurs à notre application

@login_required(login_url='sign_in')
def index(request):
    return render(request, 'gestion_stock/index.html',context={"auth_user":request.user})