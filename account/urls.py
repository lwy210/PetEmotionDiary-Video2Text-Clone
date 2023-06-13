from django.urls import path

from .views import signup_views

app_name = "account"

urlpatterns = [
    path("signup/", signup_views.signup, name="signup"),
    path("login/", signup_views.login1, name="login"),
]
