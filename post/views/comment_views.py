from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from comment.models import Comment

from ..models import Post


def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    answer = Comment(
        post=post,
        content=request.POST.get("content"),
        registered_time=timezone.now(),
        updated_time=timezone.now(),
        recommendation=0,
    )
    answer.save()
    return redirect("post:detail", post_id=post.id)
