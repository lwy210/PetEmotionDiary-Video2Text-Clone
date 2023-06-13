from account.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone


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
            return redirect("account:check_password")
        else:
            return render(request, "account/update.html")
    else:
        return render(request, "account/password_check.html")
