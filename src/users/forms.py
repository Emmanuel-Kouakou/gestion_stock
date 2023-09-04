from typing import Any, Dict
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Utilisateur, Profil


profils = Profil.objects.all()

class RegistrationForm(UserCreationForm):

    nom = forms.CharField(max_length=50)
    prenom = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=255, help_text="Veuillez entrer votre adresse email.")
    profil = forms.ModelChoiceField(queryset=profils)


    class Meta:
        model = Utilisateur
        fields = ('nom', 'prenom', 'email', 'profil', 'password1', 'password2')

## Les clean, c'est lorsque on instancie un objet avec les données du formulaire : my_object = class_form(request.POST) .. if class_form.is_valid(): my_object.cleaned_data
## On peut maintenant effectuer un bon nombre de vérification sur la valeur d'un champ et l'affecter à ce champ.
    def clean_nom(self):
        nom = self.cleaned_data['nom']
        return nom 
    
    def clean_prenom(self):
        prenom = self.cleaned_data['prenom']
        return prenom


    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        try:
            user = Utilisateur.objects.get(email=email)

        except:
            return email

        raise forms.ValidationError(f"L'email {email} que vous avez saisi existe déjà.") 


    def clean_profil(self):
        profil = self.cleaned_data['profil']
        return profil 




class UsersAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Utilisateur
        fields = ('email', 'password')

    # def clean(self):
    #     if self.is_valid():
    #         email = self.cleaned_data['email']
    #         password = self.cleaned_data['password']

    #         if not authenticate(email=email, password=password):
    #             raise forms.ValidationError("Email ou Mot de passe incorrect.")  