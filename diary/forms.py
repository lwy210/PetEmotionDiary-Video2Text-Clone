from django import forms

from diary.models import Diary
from pet.models import Pet


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ["pet", "day"]
        widgets = {
            "day": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, user, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields["pet"].queryset = Pet.objects.filter(user=user)
