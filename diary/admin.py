from django.contrib import admin

from .models import Diary, Keyword

# Register your models here.
admin.site.register(Diary)
admin.site.register(Keyword)
