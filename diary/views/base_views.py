from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from pet.models import Pet

from ..models import Diary


def index(request):
    q = Q()
    pet_id = request.GET.get("pet_id")
    if pet_id:
        q &= Q(pet_id=pet_id)

    diary_list = Diary.objects.filter(q).order_by("-day")
    print(diary_list)
    pet_list = Pet.objects.order_by("birth_day")
    context = {"diary_list": diary_list, "pet_list": pet_list}
    return render(request, "diary/diary_list.html", context)


def detail(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    pet = get_object_or_404(Pet, pk=diary.pet_id)

    context = {"diary": diary, "pet": pet}
    return render(request, "diary/diary_detail.html", context)
