from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, SignUpForm, ChangePassForm, ResetPassForm, ConfirmPassForm, EditProfile
from .models import User, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages

from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.core.mail import send_mail
from django.views import View
from django.views.generic import FormView, UpdateView,TemplateView
from django.contrib.auth import password_validation
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from threading import Thread


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
        #     form = ResetPassForm
        #     if form.is_valid():
        #         return redirect()


        

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
    



    


class ResetPassView(FormView):
    #  if "login" in request.POST:
    success_url = '/accounts/reset-password-done/'
    template_name = 'raccountss/login.html'
    form_class = ResetPassForm


    def form_valid(self, form):
        email = form.cleaned_data['email']
        user= User.objects.filter(email=email)
        if user.exists():
            token, create = Token.objects.get_or_create(user=user)
            if not create:
                    Token.objects.get(user=user).delete()
                    token = Token.objects.create(user=user)
            tr = Thread(target=send_mail,args=(
            "Reset your password",
            f"""
            please click on link for  reset password\n
            http://127.0.0.1:8000/accounts/reset-password-confirm/{token.key}""",
            "admin@mysite.com",
            [user.email],
                                                    ))
            tr.start()
            return super().form_valid(form)
        else:
            messages.add_message(
                self.request,
                messages.ERROR,
                'این ایمیل در سیستم وجود ندارد'
            )
            return redirect(self.request.path_info)
        
    
    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    


    class ResetPasswordDone(TemplateView):
        template_name = 'registrations/reset-password-done.html'

class ResetPasswordConfirm(FormView):
    template_name = 'accounts/reset-password-confirm.html'
    form_class = ConfirmPassForm
    success_url = '/accounts/reset-password-complete/'

    def form_valid(self, form):
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']

        if password1 == password2:
            try:
                validate_password(password1)
            except Exception as e:
                messages.error(self.request, "پسورد باید 8 کارکتر شامل حروف بزرگ و کوچک و علائم باشد  ")
                return redirect(self.request.path_info)
            token = self.kwargs.get('token')
            try:
                access_token = AccessToken(token)
                user_id = access_token['user_id']
                user = User.objects.get(id=user_id)
                user.set_password(password1)
                user.save()
                messages.add_message(
                    self.request,
                    messages.SUCCESS,
                    'رمز عبور با موفقیت تغییر یافت'
                )
                return super().form_valid(form)
            except Exception as e:
                messages.error(self.request, "توکن منقضی شده اسن  ")
                return redirect('/accounts/reset-password/')
        else:
            messages.error(self.request, "پسوردها با هم مطابقت ندارند")
            return redirect(self.request.path_info)

class ResetPasswordComplete(TemplateView):
    template_name = 'registrations/forget-password-complete.html'

