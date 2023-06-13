from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from comment.forms import CommentForm
from comment.models import Comment

from ..models import Post


def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.registered_time = timezone.now()
            comment.updated_time = timezone.now()
            comment.recommendation = 0
            comment.post = post
            comment.save()
            return redirect("post:detail", post_id=post.id)
    else:
        return HttpResponseNotAllowed("Only POST is possible.")
    context = {"post": post, "form": form}
    return render(request, "post/post_detail.html", context)
