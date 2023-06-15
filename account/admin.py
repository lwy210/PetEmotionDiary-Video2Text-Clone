from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "birth_day",
        "is_admin",
        "user_name",
        "nick_name",
        "create_time",
        "update_time",
    )
    list_filter = ("is_admin",)
    ordering = ("create_time",)
    search_fields = ("email",)


# Register your models here.
admin.site.register(User, UserAdmin)
