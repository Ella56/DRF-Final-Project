from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User, Profile
from django.contrib.auth import password_validation



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["email", "password1", "password2"]

class ResetPassForm(forms.Form):
    email = forms.EmailField()



class ChangePassForm(forms.Form):
    current_password = forms.CharField(max_length=15,widget=forms.PasswordInput, label="Current_Password")
    password1 = forms.CharField(max_length=15, widget=forms.PasswordInput, label="New_Password")
    password2 = forms.CharField(max_length=15, widget=forms.PasswordInput, label="Confirm_New_Password")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)


    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The new passwords do not match")
        

        if password1:
            try:
                password_validation.validate_password(password1, user=self.user)
            except forms.ValidationError as error:
                self.add_error("password1", error)

        return cleaned_data
    
    def clean_current_password(self):
        current_password = self.cleaned_data.get ("current_password")
        if self.user and not self.user.check_password(current_password):
            raise forms.ValidationError("Your current password is incorrect.")
        return current_password

    # class Meta:
    #     fields = ['current_password', 'password1', 'password2']

    # def __init__(self, *args, **kwargs):
    
    #     super().__init__(*args, **kwargs)
    #     self.fields['old_password'].label="Current_Password"
    #     self.fields['new_password1'].label="New_Password"
    #     self.fields['new_password2'].label="Confirm_New_Password"
    


class ConfirmPassForm(forms.Form):
    pass1 = forms.CharField(max_length=15)
    pass2 = forms.CharField(max_length=15)



class EditProfile(forms.ModelForm):
      
      class Meta:
        model = Profile
        fields = ["fname", "lname", "phone", "address", "postal_code"]