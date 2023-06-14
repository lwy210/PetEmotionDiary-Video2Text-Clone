from account.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import login


@login_required(login_url="account:login")
def update(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.update_time = timezone.now()
            user.save()
            return redirect("account:logout_test")
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
                request.user.set_password(new_password)
                request.user.save()
                login(request, request.user)
                return redirect("account:logout_test")
            else:
                messages.error(request, "새 비밀번호를 다시 확인해주세요.")
        else:
            messages.error(request, "현재 비밀번호가 틀렸습니다.")

    return render(request, "account/password_update.html")
