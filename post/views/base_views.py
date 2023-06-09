from django.shortcuts import get_object_or_404, render

from ..models import Post


def index(request):
    category = request.GET.get("category")
    kind = request.GET.get("kind")

    post_list = Post.objects.order_by("-registered_time")

    if category:
        post_list = post_list.filter(category=category)

    if kind:
        post_list = post_list.filter(kind=kind)

    context = {"post_list": post_list}
    return render(request, "post/post_list.html", context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "post/post_detail.html", context)
