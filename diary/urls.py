from django.urls import path

from .views import base_views

app_name = "diary"

urlpatterns = [
    path("", base_views.index, name="index"),
    path("<int:diary_id>/", base_views.detail, name="detail"),
]
