from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from .forms import ResetPassForm


app_name = "accounts"

urlpatterns = [
    path("login-signup/", LoginView.as_view(), name="login-signup"),
    path("logout/",LogoutView.as_view(), name="logout"),
    path("edit-profile/", EditProfileView.as_view(), name = "edit-profile"),
    path("change-password/", ChangePasswordView.as_view(), name = "change-password"),
    # path("api/v1/",include("accounts.api.v1.urls")),
    path("password-reset/",auth_views.PasswordResetView.as_view(form_class=ResetPassForm),name="password-reset"),
    path("password-reset-done/", auth_views.PasswordResetDoneView.as_view(), name="password-reset-done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name = "password-reset-confirm"),
    path('password-reset-done/', auth_views.PasswordResetCompleteView.as_view(), name="password-reset-complete")

]