from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from ..forms import PetForm
from ..models import Personality, Pet


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
    context = {"form": form, "operation": "create"}
    return render(request, "pet/pet_form.html", context)


@login_required(login_url="account:login")
def pet_modify(request, pet_id, request_url):
    pet = get_object_or_404(Pet, pk=pet_id)
    if request.user != pet.user:
        messages.error(request, "수정권한이 없습니다")
        return redirect("pet:detail", pet_id=pet.id)
    if request.method == "POST":
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.save()

            personality, created = Personality.objects.get_or_create(
                pet=pet,
                defaults={
                    "activity": form.cleaned_data["activity"],
                    "relationship": form.cleaned_data["relationship"],
                    "proto_dog": form.cleaned_data["proto_dog"],
                    "dependence": form.cleaned_data["dependence"],
                },
            )
            if not created:
                personality.activity = form.cleaned_data["activity"]
                personality.relationship = form.cleaned_data["relationship"]
                personality.proto_dog = form.cleaned_data["proto_dog"]
                personality.dependence = form.cleaned_data["dependence"]
                personality.save()

            if request_url == "list":
                return redirect("pet:index")
            else:
                return redirect("pet:detail", pet_id=pet.id)
    else:
        personality = Personality.objects.filter(pet=pet).first()
        if personality:
            form = PetForm(
                instance=pet,
                initial={
                    "activity": personality.activity,
                    "relationship": personality.relationship,
                    "proto_dog": personality.proto_dog,
                    "dependence": personality.dependence,
                },
            )
        else:
            form = PetForm(instance=pet)
    context = {"form": form, "operation": "modify", "pet": pet}
    return render(request, "pet/pet_form.html", context)


@login_required(login_url="account:login")
def pet_delete(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    if request.user != pet.user:
        messages.error(request, "삭제권한이 없습니다")
        return redirect("pet:detail", pet_id=pet.id)
    pet.delete()
    return redirect("pet:index")
