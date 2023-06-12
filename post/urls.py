from django.urls import path

from .views import base_views

app_name = "post"

urlpatterns = [
    # base_views.py
    path("", base_views.index, name="index"),
    path("<int:post_id>/", base_views.detail, name="detail"),
]
