from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin 

from .models import Utilisateur, Profil


class UtilisateurAdmin(UserAdmin):
    list_display = ('email', 'nom', 'prenom', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email',)
    readonly_fields = ('id', 'date_joined', 'last_login')


    list_filter = ()
    fieldsets = ()

    ordering = ('date_joined',)
    filter_horizontal = ()


admin.site.register(Profil)
admin.site.register(Utilisateur, UtilisateurAdmin)    

#1021