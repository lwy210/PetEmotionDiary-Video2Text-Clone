import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from ..models import Diary


@login_required(login_url="account:login")
def get_diarys(request):
    diarys = Diary.objects.all()
    return JsonResponse({"diarys": list(diarys.values())})


@login_required(login_url="account:login")
def get_diary_info(request, diary_id):
    diary = Diary.objects.get(id=diary_id)
    keywords = diary.keywords.all()
    bookmark = diary.bookmark
    title = diary.title
    keywords_list = [keyword.word for keyword in keywords]

    return JsonResponse(
        {"keywords": keywords_list, "bookmark": bookmark, "title": title}
    )
