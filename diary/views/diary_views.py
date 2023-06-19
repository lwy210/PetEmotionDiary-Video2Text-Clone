from urllib.parse import urlencode

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, resolve_url

from ..models import Diary


@login_required(login_url="account:login")
def diary_bookmark(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    if request.user == diary.user:
        diary.bookmark = not diary.bookmark
        diary.save()
    query_params = {}
    page = request.POST.get("page")
    keyword = request.POST.get("keyword")
    pet_id = request.POST.get("pet_id")

    if page:
        query_params["page"] = page
    if keyword:
        query_params["keyword"] = keyword
    if pet_id:
        query_params["pet_id"] = pet_id

    query_string = urlencode(query_params)

    return HttpResponseRedirect(
        f"{resolve_url('diary:index')}?{query_string}#diary_{diary.id}"
    )
