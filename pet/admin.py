from django.contrib import admin

from .models import Personality, Pet


class PersonalityInline(admin.StackedInline):
    model = Personality
    max_num = 1


class PetAdmin(admin.ModelAdmin):
    inlines = [PersonalityInline]


admin.site.register(Pet, PetAdmin)
admin.site.register(Personality)
