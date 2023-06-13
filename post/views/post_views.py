from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from ..forms import PostForm
from ..models import Post


@login_required(login_url="account:login")
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


@login_required(login_url="account:login")
def post_modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.user:
        messages.error(request, "수정권한이 없습니다")
        return redirect("post:detail", post_id=post.id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.updated_time = timezone.now()  # 수정일시 저장
            post.save()
            return redirect("post:detail", post_id=post.id)
    else:
        form = PostForm(instance=post)
    context = {"form": form}
    return render(request, "post/post_form.html", context)


@login_required(login_url="account:login")
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.user:
        messages.error(request, "삭제권한이 없습니다")
        return redirect("post:detail", post_id=post.id)
    post.delete()
    return redirect("post:index")
