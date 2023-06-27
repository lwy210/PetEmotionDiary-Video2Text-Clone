from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="account:login")
def mypage(request):
    data = {"user": request.user}
    return render(request, "account/mypage.html", data)
