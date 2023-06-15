from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from ..models import Pet


@login_required(login_url="account:login")
def index(request):
    pet_list = Pet.objects.filter(user_id=request.user.id)
    context = {"pet_list": pet_list}
    return render(request, "pet/pet_list.html", context)


def detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)

    context = {"pet": pet}
    return render(request, "pet/pet_detail.html", context)
