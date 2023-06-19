from django.urls import path

from .views import base_views, diary_views

app_name = "diary"

urlpatterns = [
    path("", base_views.index, name="index"),
    path("<int:diary_id>/", base_views.detail, name="detail"),
    path("bookmark/", diary_views.diary_bookmark, name="diary_bookmark_base"),
    path("bookmark/<int:diary_id>/", diary_views.diary_bookmark, name="diary_bookmark"),
]
