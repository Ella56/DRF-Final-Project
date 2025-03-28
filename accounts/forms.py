from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["email", "password1", "password2"]

class ResetPassForm(forms.Form):
    email = forms.EmailField()



class ChangePassForm(forms.Form):
    password1 = forms.CharField(max_length=15)
    password2 = forms.CharField(max_length=15)




class ConfirmPassForm(forms.Form):
    pass1 = forms.CharField(max_length=15)
    pass2 = forms.CharField(max_length=15)

class EditProfile(forms.ModelForm):
    pass
#       class Meta:
#         model = Profile
#         fields = ["first_name", "last_name", "phone", "address", "postal_code"]