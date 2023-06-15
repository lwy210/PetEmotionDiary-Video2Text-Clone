from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..forms import PetForm


@login_required(login_url="account:login")
def pet_create(request):
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect("pet:index")
    else:
        form = PetForm()
    context = {"form": form}
    return render(request, "pet/pet_form.html", context)
