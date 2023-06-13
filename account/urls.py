from django.urls import path
from django.contrib.auth import views as auth_views

from .views import signup_views, update_views

app_name = "account"

urlpatterns = [
    path("signup/", signup_views.signup, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="account/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("logout/test", signup_views.logout_test, name="logout_test"),
    path("update/", update_views.update, name="update"),
    path("check/", update_views.check_password, name="check_password"),
]
