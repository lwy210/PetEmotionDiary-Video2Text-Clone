from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..forms import PetForm
from ..models import Personality


@login_required(login_url="account:login")
def pet_create(request):
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()

            personality = Personality(
                pet=pet,
                activity=form.cleaned_data["activity"],
                relationship=form.cleaned_data["relationship"],
                proto_dog=form.cleaned_data["proto_dog"],
                dependence=form.cleaned_data["dependence"],
            )
            personality.save()
            return redirect("pet:index")
    else:
        form = PetForm()
    context = {"form": form}
    return render(request, "pet/pet_form.html", context)
