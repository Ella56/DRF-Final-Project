from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile
from captcha.fields import CaptchaField



class LoginForm(forms.Form):
    pass


class SignUpForm(UserCreationForm):
    pass


class ChangePassForm(forms.Form):
    pass


class ResetPassForm(forms.Form):
    pass

class ConfirmPassForm(forms.Form):
    pass

class EditProfile(forms.ModelForm):
    pass