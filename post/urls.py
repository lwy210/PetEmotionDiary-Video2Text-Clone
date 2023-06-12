from django.urls import path

from .views import base_views, post_views

app_name = "post"

urlpatterns = [
    # base_views.py
    path("", base_views.index, name="index"),
    path("<int:post_id>/", base_views.detail, name="detail"),
    path("create/", post_views.post_create, name="post_create"),
    path("modify/<int:post_id>/", post_views.post_modify, name="post_modify"),
    path("delete/<int:post_id>/", post_views.post_delete, name="post_delete"),
]
