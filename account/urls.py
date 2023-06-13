from django.urls import path
from django.contrib.auth import views as auth_views

from .views import signup_views

app_name = "account"

urlpatterns = [
    path("signup/", signup_views.signup, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="account/login.html"),
        name="login",
    ),
]
