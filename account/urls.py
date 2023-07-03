from django.urls import path
from django.contrib.auth import views as auth_views

from .views import signup_views, update_views, mypage_views
from .views.kakao import kakao_views

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
    path("update/password", update_views.update_password, name="update_password"),
    path("update/delete", update_views.delete, name="delete"),
    path("update/withdraw", update_views.withdraw, name="withdraw"),
    path("login/kakao", kakao_views.KakaoSignInView, name="kakao"),
    path(
        "login/kakao/callback/",
        kakao_views.KaKaoSignInCallBackView,
        name="kakao_callback",
    ),
    path("mypage", mypage_views.mypage, name="mypage"),
    path("termofservice", signup_views.terms_of_service, name="terms"),
]
