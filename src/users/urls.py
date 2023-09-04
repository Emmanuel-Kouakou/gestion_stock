"""
URL configuration for gestion_stock project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import register, logout_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', register, name='users-register'),
    path('logout/', logout_view, name='users-logout'),
    
     # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_reset/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/password_reset/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="users/password_reset/password_reset_form.html", email_template_name="users/password_reset/password_reset_email.html", subject_template_name="users/password_reset/password_reset_subject.txt"), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset/password_reset_complete.html'), name='password_reset_complete'),
]
