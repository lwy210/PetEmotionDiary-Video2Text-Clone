from django import forms

from diary.models import Diary
from pet.models import Pet


class DiaryForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Diary
        fields = ["pet", "day", "content", "title"]
        widgets = {
            "day": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields["pet"].queryset = Pet.objects.filter(user=user)
