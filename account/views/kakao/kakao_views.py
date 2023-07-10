from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import login
import requests
from account.models import User


def KakaoSignInView(request):
    if request.user.is_authenticated:
        raise Exception("이미 로그인이 되어 있습니다.")
    app_key = settings.KAKAO_KEY
    redirect_uri = "http://petemotiondiary.site/account/login/kakao/callback/"
    kakao_auth_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"
    return redirect(f"{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}")


def KaKaoSignInCallBackView(request):
    auth_code = request.GET.get("code")
    kakao_token_api = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": settings.KAKAO_KEY,
        "redirection_uri": "http://petemotiondiary.site/accounts/signin/kakao/callback/",
        "code": auth_code,
    }

    token_response = requests.post(kakao_token_api, data=data)

    access_token = token_response.json().get("access_token")

    user_info_response = requests.get(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer ${access_token}"},
    )

    profile_json = user_info_response.json()
    kakao_account = profile_json.get(
        "kakao_account",
        {
            "profile": {"nickname": "임시이름"},
            "email": "임시이메일@gmail.com",
            "birthday": "0101",
        },
    )

    profile = kakao_account.get("profile", {"nickname": "임시이름"})
    nickname = profile.get("nickname")
    email = kakao_account.get("email", "임시이메일@naver.com")
    birthday = kakao_account.get("birthday", "0101")

    user = User.objects.get_or_none(email=email)

    if user is None:
        user = User.objects.create_user(
            email=email,
            nick_name=nickname,
            user_name=nickname,
            birth_day=birthday,
        )

    login(request, user)
    return redirect("main")
