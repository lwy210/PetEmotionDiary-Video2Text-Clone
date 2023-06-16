from django.shortcuts import render

from ..models import Diary


def index(request):
    diary_list = Diary.objects.order_by("-day")

    context = {"diary_list": diary_list}
    return render(request, "diary/diary_list.html", context)
