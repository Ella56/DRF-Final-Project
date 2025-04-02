from django import forms
from accounts.models import Profile


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'postal_code']