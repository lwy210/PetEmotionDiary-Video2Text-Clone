from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from ..models import Post


def index(request):
    page = request.GET.get("page", "1")  # 페이지
    kw = request.GET.get("kw", "")  # 검색어
    q = Q()
    category = request.GET.get("category")
    kind = request.GET.get("kind")

    if category:
        q &= Q(category=category)

    if kind:
        q &= Q(kind=kind)

    post_list = Post.objects.filter(q).order_by("-registered_time")
    if kw:
        post_list = post_list.filter(
            Q(title__icontains=kw) | Q(content__icontains=kw)  # 제목 검색
        ).distinct()
    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {"post_list": page_obj, "page": page, "kw": kw}
    return render(request, "post/post_list.html", context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "post/post_detail.html", context)
