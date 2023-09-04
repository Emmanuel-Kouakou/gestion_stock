from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

# Utilisation du UserManager pour créer un nouveau utilisateur ainsi qu'un superuser
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, nom="", prenom=""):

        if not email:
            raise ValueError("Vous devez entrer un email.")
        
        user = self.model(email=self.normalize_email(email))

        user.set_password(password)

        user.nom = nom
        user.prenom = prenom
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password=None, nom="", prenom=""):
        user=self.create_user(email=email, password=password, nom=nom, prenom=prenom)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.profil_id = 1

        user.save(using=self._db)

        return user



class Profil(models.Model):
    libelle=models.CharField(max_length=30)

    def __str__(self):
        return self.libelle


def get_profile_image_filepath(self):
    return f'profil_images/{self.pk}/{"profile_image.png"}'

def get_default_profil_image():
    return "default_image/logo_1080_1080.png" 


# Notre modèle utilisateur
class Utilisateur(AbstractBaseUser):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=255, blank=False)

    profil = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    last_login = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    # profil_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profil_image)

    objects = MyUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
    

    # def get_profile_image_filename(self):
    #     return str(self.profil_image)[str(self.profil_image).index(f'profile_images/{self.pk}/'):]

    def has_perm(self, perm, obj=None):
        #"Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        #"Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    # @property
    # def is_staff(self):
    #     #"Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_staff





    
    
    
    

    
    
