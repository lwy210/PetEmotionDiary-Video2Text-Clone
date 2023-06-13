from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
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
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("post:detail", post_id=post.id), comment.id
                )
            )
    else:
        return HttpResponseNotAllowed("Only POST is possible.")
    context = {"post": post, "form": form}
    return render(request, "post/post_detail.html", context)


def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.user:
        messages.error(request, "수정권한이 없습니다")
        return redirect("post:detail", post_id=comment.post.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.updated_time = timezone.now()
            comment.save()
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("post:detail", post_id=comment.post.id), comment.id
                )
            )
    else:
        form = CommentForm(instance=comment)
    context = {"answer": comment, "form": form}
    return render(request, "post/comment_form.html", context)


def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.user:
        messages.error(request, "삭제권한이 없습니다")
    else:
        comment.delete()
    return redirect("post:detail", post_id=comment.post.id)
