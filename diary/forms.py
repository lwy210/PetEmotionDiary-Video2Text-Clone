from django import forms

from diary.models import Diary
from pet.models import Pet


class DiaryForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, required=False)
    title = forms.CharField(required=False)
    video = forms.FileField(
        widget=forms.FileInput(attrs={"class": "form-control", "id": "video"}),
        required=False,
    )

    class Meta:
        model = Diary
        fields = ["pet", "day", "content", "title", "video"]
        widgets = {
            "day": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields["pet"].queryset = Pet.objects.filter(user=user)
