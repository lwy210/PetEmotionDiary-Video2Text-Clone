from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from account.forms import UserCreationForm


def signup(request):
    if request.user.is_authenticated:
        raise Exception("이미 로그인이 되어 있습니다.")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect("main")
    else:
        form = UserCreationForm()

    return render(request, "account/signup.html", {"form": form})


def logout_test(request):
    return render(request, "account/logout.html")
