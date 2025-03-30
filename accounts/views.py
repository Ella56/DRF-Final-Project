from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, SignUpForm, ChangePassForm, ResetPassForm, ConfirmPassForm, EditProfile
from .models import User, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import password_validation
# from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.views import View
from django.views.generic import FormView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.middleware.csrf import get_token
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, PasswordChangeView

# Create your views here.


class LoginView(View):
    template_name = "accounts/login.html"
    success_url="/"


    def get(self, request):
        # csrf_token = get_token(request)
        # print("token for get", csrf_token)

        return render(request, self.template_name,{
            "login_form": LoginForm(),
            "signup_form": SignUpForm(),
            "reset_form": ResetPassForm(),
        })
    
        
    
    def post(self, request):
        # print("post data",request.POST)
        # print("csrf taken from post data",request.POST.get('csrfmiddlewaretoken'))
        # print("expected token",request.META.get('CSRD_COOKIE'))


        if "login" in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(self.request, user)
                    messages.add_message(request,messages.SUCCESS, "Account created successfully!")
                    return redirect(self.success_url)
                else:
                    messages.add_message(self.request, messages.ERROR, "Invalid credintial")
                    return redirect(self.request.path_info)
            else:
                messages.add_message(self.request, messages.ERROR, "Invalid Data")
                return redirect(self.request.path_info)
                
        elif "signup" in request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user) 
                return redirect(self.request.path_info)
            else:
                # for field, errors in form.errors.items():
                #     for error in errors:
                #         messages.error(request, f'{field}:{error}')

                messages.add_message(request, messages.ERROR, "Invalid Data")
                return redirect(self.request.path_info)
            

        # elif "reset-password" in request.POST:


        

class LogoutView(LogoutView):
    next_page = "/"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['message'] = 'You have been Logged out'
    #     return context



class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = EditProfile
    template_name = "accounts/profile.html"
    success_url = "/"

    pk_url_kwarg = None

    def get_object(self, queryset = None):
        profile = Profile.objects.get(user=self.request.user)
        return profile


    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, "Profile Updated Successfully!")
        return response
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please correct the errors")
        return redirect(self.request.path_info)
    


class ChangePasswordView(LoginRequiredMixin,FormView):

    form_class = ChangePassForm
    template_name = "accounts/change_password.html"
    success_url="/"


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    

    def form_valid(self, form):
        user = self.request.user
        new_password = form.cleaned_data['password1']

        user.set_password(new_password)
        user.save()
        update_session_auth_hash(self.request, user)
        messages.add_message(self.request, messages.SUCCESS, "Your password was successfully updated!")
        return super().form_valid(form)
    


    def form_invalid(self, form):
        print("forms errors", form.errors)
        messages.add_message(self.request, messages.ERROR, "Please correct the errors")
        return redirect(self.request.path_info)
    



    

    