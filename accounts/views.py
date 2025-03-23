from django.shortcuts import render
from .forms import LoginForm, SignUpForm, ChangePassForm, ResetPassForm, ConfirmPassForm, EditProfile, Captcha
from .models import User, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth import password_validation
# from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class LoginView(FormView):
    pass