from django.shortcuts import render, redirect
from django.core.validators import validate_email
from .models import Profil, Utilisateur

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm

# from .admin import UserCreationForm


# Create your views here.

# Vue d'inscriptions des utilisateurs

# @login_required(login_url='sign_in')
# def register(request):

#     error = False
#     message=""

#     profils = Profil.objects.all()

#     if request.method == 'POST':

#         nom = request.POST['nom']
#         prenom = request.POST['prenom']
#         email = request.POST['email']
#         profil_id = request.POST['profil_id']
#         password = request.POST['password']
#         repassword = request.POST['repassword']
    

#         try:
#             validate_email(email)
#         except:
#             error="True"
#             message="Entrer un email valide s'il vous plaît !"
#             return render(request, 'users/register.html', context={"profils":profils,"error":error, "message":message})

        
#         user = Utilisateur.objects.filter(email=email).first()

#         if user and error==False:
#             error=True
#             message="Cet email existe déjà !"
#             return render(request, 'users/register.html', context={"profils":profils,"error":error, "message":message})
            


#         if error==False and password!=repassword:
#             error=True
#             message="Les mots de passes entrés ne correspondent pas." 
#             return render(request, 'users/register.html', context={"profils":profils,"error":error, "message":message})

        
#     #     Utilisateur.objects.create_user(email=email, nom=nom, prenom=prenom)  

#     #     user = Utilisateur.objects.get(email=email)
#     #     user.profil_id = profil_id
#     #     user.save() 


#     context={"profils":profils,"error":error, "message":message}           


#     return render(request, 'users/register.html',context=context )

@login_required(login_url='sign_in')
def register(request):
    
    profils = Profil.objects.all()
    context = {}

    error = False
    message=""

    context['profils'] = profils 

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password1']
        repassword = request.POST['password2']



        user = Utilisateur.objects.filter(email=email).first()

        if user and error==False:
            error=True
            message=f"L'email {email} que vous avez saisi existe déjà."
            context['error']=error
            context['message']=message
            return render(request, 'users/register.html', context=context)
        

        if error==False and password!=repassword:
            error=True
            message="Les mots de passes entrés ne correspondent pas." 
            context['error']=error
            context['message']=message
            return render(request, 'users/register.html', context=context)
        
        form = RegistrationForm(request.POST)  

        if form.is_valid():
            form.save()

            return render(request, 'users/register.html', context=context)

        else:        
            context['registration_form'] = form         


    return render(request, 'users/register.html', context=context)


# Vue de connexion des utilisateurs à notre application
def sign_in(request):
    
    error = False
    message = ""

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        # remember = True if request.POST['remember'] else False

        try:
            validate_email(email)
        except:
            error="True"
            message="Entrer un email valide s'il vous plaît !"
            context['error']=error
            context['message']=message
            return render(request, 'users/sign_in.html', context=context)
        
        user = Utilisateur.objects.filter(email=email).first()

        if not user:
            error=True
            message="L'utilisateur que vous avez saisi n'existe pas."
            context['error']=error
            context['message']=message
            return render(request, 'users/sign_in.html', context=context)
        
        else:
            if user.is_active==True:
                auth_user = authenticate(request=request, email=email, password=password)

                if auth_user is None:
                    error=True
                    message="Mot de passe incorrect"
                    context['error']=error
                    context['message']=message
                    return render(request, 'users/sign_in.html', context=context)

                else:
                    login(request, auth_user)

                    return redirect('index')
                
            else:
                error=True
                message="Vous n'êtes pas active. Veuillez s'il vous plaît contacter l'administrateur système."
                return render(request, 'users/sign_in.html', context={"error":error, "message":message})



    return render(request, 'users/sign_in.html')


@login_required(login_url='sign_in')
def logout_view(request):

    logout(request)

    return redirect('sign_in')




    
