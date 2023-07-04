import json
import os
import tempfile
from io import BytesIO
from urllib.parse import urlencode, urlparse

import boto3
import cv2
import numpy as np
from botocore.exceptions import NoCredentialsError
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.utils import timezone
from PIL import Image

from ai.views import diary_views

# from ai.views.diary_views import create_diary
from pet.models import Personality, Pet

from ..forms import DiaryForm
from ..models import Diary, Keyword


# ========================= prod start =======================
def upload_file_to_s3(file_path, s3_bucket, s3_key):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION,
    )

    try:
        s3.upload_file(file_path, s3_bucket, s3_key)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


@login_required(login_url="account:login")
def diary_create_before(request):
    if request.method == "POST":
        form = DiaryForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            # <- 보낼거 함수에 ->
            diary = form.save(commit=False)
            user_id = request.user.id
            pet_id = form.cleaned_data["pet"].id
            pet = Pet.objects.get(id=pet_id)
            personality = Personality.objects.get(pet=pet)
            content_list = request.POST.getlist("content[]")
            diary.registered_time = timezone.now()
            diary.updated_time = timezone.now()
            diary.user_id = user_id
            diary.save()

            input = {
                "pet": pet,
                "personality": personality,
                "add_content": content_list,
                "video": diary.video.url,
                "diary_id": diary.id,
            }

            result = diary_views.create_diary(input)

            local_file_path = f"static/media/split_imgs/{diary.id}frame_0.jpg"
            s3_bucket = settings.AWS_STORAGE_BUCKET_NAME
            s3_key = f"media/diary_images/{diary.id}frame_0.jpg"
            upload_file_to_s3(local_file_path, s3_bucket, s3_key)
            diary.thumbnail = f"{settings.MEDIA_URL}diary_images/{diary.id}frame_0.jpg"
            diary.save()

            content_list = request.POST.getlist("content[]")

            context = {
                "form": form,
                "content": result["diary_content"],
                "title": result["title"],
                "video": diary.video.url,
                "thumbnail": diary.thumbnail,
                "keywords": result["keywords"],
                "diary_id": diary.id,
            }

            return render(request, "diary/diary_result_form.html", context)
    else:
        form = DiaryForm(request.user)
    context = {"form": form}
    return render(request, "diary/diary_form.html", context)


# ========================= prod end =======================


# ========================= local start =======================
# def save_thumbnail(video_path, thumbnail_path):
#     vidcap = cv2.VideoCapture(video_path)
#     success, image = vidcap.read()
#     if success:
#         cv2.imwrite(thumbnail_path, image)


# @login_required(login_url="account:login")
# def diary_create_before(request):
#     if request.method == "POST":
#         form = DiaryForm(request.user, request.POST, request.FILES)
#         if form.is_valid():
#             diary = form.save(commit=False)
#             user_id = request.user.id
#             pet_id = form.cleaned_data["pet"].id
#             pet = Pet.objects.get(id=pet_id)
#             personality = Personality.objects.get(pet=pet)
#             content_list = request.POST.getlist("content[]")
#             diary.registered_time = timezone.now()
#             diary.updated_time = timezone.now()
#             diary.user_id = user_id
#             diary.save()

#             fs = FileSystemStorage()
#             video_path = fs.path(diary.video.name)

#             thumbnail_path = os.path.join(
#                 settings.MEDIA_ROOT,
#                 "diary_images/thumbnail" + str(diary.id) + ".jpg",
#             )

#             save_thumbnail(video_path, thumbnail_path)
#             diary.thumbnail = thumbnail_path
#             diary.save()

#             input = {
#                 "pet": pet,
#                 "personality": personality,
#                 "add_content": content_list,
#                 "video": "static/" + diary.video.url,
#                 "diary_id": diary.id,
#             }

#             result = diary_views.create_diary(input)

#             content_list = request.POST.getlist("content[]")

#             context = {
#                 "form": form,
#                 "content": result["diary_content"],
#                 "title": result["title"],
#                 "video": diary.video.url,
#                 "thumbnail": diary.thumbnail.url,
#                 "keywords": result["keywords"],  # 생성된 keyword
#                 "diary_id": diary.id,
#             }

#             return render(request, "diary/diary_result_form.html", context)
#     else:
#         form = DiaryForm(request.user)
#     context = {"form": form}
#     return render(request, "diary/diary_form.html", context)


# ========================= local end =======================


@login_required(login_url="account:login")
def diary_create(request):
    if request.method == "POST":
        form = DiaryForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = request.user
            diary.registered_time = timezone.now()
            diary.updated_time = timezone.now()
            diary.content = request.POST.get("content")
            diary.title = request.POST.get("title")
            diary.id = request.POST.get("diary_id")
            diary.video = request.POST.get("video")
            diary.thumbnail = request.POST.get("thumbnail")

            checked_list_str = request.POST["keyword_list"]
            checked_list = json.loads(checked_list_str)
            keywords_list = []

            for keyword in checked_list:
                if keyword:
                    keyword_obj, created = Keyword.objects.get_or_create(word=keyword)
                    keywords_list.append(keyword_obj)

            diary.save()
            diary.keywords.set(keywords_list)

            return redirect("diary:detail", diary_id=diary.id)
    else:
        form = DiaryForm(request.user)
    context = {"form": form}
    return render(request, "diary/diary_result_form.html", context)


@login_required(login_url="account:login")
def diary_modify(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    if request.user != diary.user:
        messages.error(request, "수정권한이 없습니다")
        return redirect("diary:detail", diary_id=diary.id)
    if request.method == "POST":
        form = DiaryForm(request.user, request.POST, request.FILES, instance=diary)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.updated_time = timezone.now()  # 수정일시 저장
            added_list_str = request.POST["keyword_list"]
            added_list = json.loads(added_list_str)
            keywords_list = []

            for keyword in added_list:
                if keyword:
                    keyword_obj, created = Keyword.objects.get_or_create(word=keyword)
                    keywords_list.append(keyword_obj)
                    diary.keywords.add(keyword_obj)

            diary.save()

            return redirect("diary:detail", diary_id=diary.id)
    else:
        form = DiaryForm(user=request.user, instance=diary)
    context = {"form": form, "diary": diary}
    return render(request, "diary/diary_modify.html", context)


@login_required(login_url="account:login")
def diary_delete(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    if request.user != diary.user:
        messages.error(request, "삭제권한이 없습니다")
        return redirect("diary:detail", diary_id=diary.id)
    diary.delete()
    return redirect("diary:index")


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
        f"{resolve_url('diary:index_list')}?{query_string}#diary_{diary.id}"
    )
