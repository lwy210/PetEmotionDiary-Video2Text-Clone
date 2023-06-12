from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from ..models import Post


def index(request):
    q = Q()
    category = request.GET.get("category")
    kind = request.GET.get("kind")

    if category:
        q &= Q(category=category)

    if kind:
        q &= Q(kind=kind)

    post_list = Post.objects.filter(q).order_by("-registered_time")
    context = {"post_list": post_list}
    return render(request, "post/post_list.html", context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "post/post_detail.html", context)
