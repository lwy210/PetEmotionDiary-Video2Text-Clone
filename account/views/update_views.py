from account.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.exceptions import ValidationError
import re


@login_required(login_url="account:login")
def update(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.update_time = timezone.now()
            user.save()
            data = {"user": request.user}
            return render(request, "account/mypage.html", data)
    else:
        form = UserChangeForm(instance=request.user)
    context = {
        "form": form,
    }

    return render(request, "account/update.html", context)


@login_required(login_url="account:login")
def check_password(request):
    if request.method == "POST":
        password1 = request.POST.get("password")
        if not request.user.check_password(password1):
            messages.error(request, "비밀번호가 틀렸습니다.")
            return redirect("account:check_password")
        else:
            return render(request, "account/update.html")
    else:
        return render(request, "account/password_check.html")


@login_required(login_url="account:login")
def update_password(request):
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        if request.user.check_password(current_password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                if len(new_password) < 8:
                    messages.error(request, "비밀번호는 8자리 이상이어야 합니다.")
                    return redirect("account:update_password")
                if not re.search(r"[a-zA-Z]", new_password):
                    messages.error(request, "비밀번호는 하나 이상의 영문이 포함되어야 합니다.")
                    return redirect("account:update_password")
                if not re.search(r"\d", new_password):
                    messages.error(request, "비밀번호는 하나 이상의 숫자가 포함되어야 합니다.")
                    return redirect("account:update_password")
                if not re.search(r"[!@#$%^&*()]", new_password):
                    messages.error(
                        request, "비밀번호는 적어도 하나 이상의 특수문자(!@#$%^&*())가 포함되어야 합니다."
                    )
                    return redirect("account:update_password")
                request.user.set_password(new_password)
                request.user.update_time = timezone.now()
                request.user.save()
                login(request, request.user)
                data = {"user": request.user}
                return render(request, "account/mypage.html", data)
            else:
                messages.error(request, "새 비밀번호를 다시 확인해주세요.")
        else:
            messages.error(request, "현재 비밀번호가 틀렸습니다.")

    return render(request, "account/password_update.html")


@login_required(login_url="account:login")
def delete(request):
    if request.method == "POST":
        request.user.delete()
        logout(request)
        return render(request, "account/login.html")

    return render(request, "account/delete.html")
