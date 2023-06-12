from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from ..forms import PostForm


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.registered_time = timezone.now()
            post.updated_time = timezone.now()
            post.recommendation = 0
            post.save()
            return redirect("post:index")
    else:
        form = PostForm()
    context = {"form": form}
    return render(request, "post/post_form.html", context)
