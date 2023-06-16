from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from pet.models import Pet

from ..models import Diary


def index(request):
    page = request.GET.get("page", "1")  # 페이지
    q = Q()
    pet_id = request.GET.get("pet_id")
    if pet_id:
        q &= Q(pet_id=pet_id)

    diary_list = Diary.objects.filter(q).order_by("-day")
    print(diary_list)
    pet_list = Pet.objects.order_by("birth_day")
    paginator = Paginator(diary_list, 5)  # 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {"diary_list": page_obj, "pet_list": pet_list}
    return render(request, "diary/diary_list.html", context)


def detail(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    pet = get_object_or_404(Pet, pk=diary.pet_id)

    context = {"diary": diary, "pet": pet}
    return render(request, "diary/diary_detail.html", context)
