from django.urls import path, include
from .views import *


app_name = "accounts"

urlpatterns = [
    path("login-signup/", LoginView.as_view(), name="login-signup"),
    path("logout/",logout_user, name="logout"),
]