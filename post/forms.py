from django import forms

from post.models import Post


class PostForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ("자유게시판", "free_type"),
        ("사진자랑", "brag_type"),
        ("고민공유", "worry_type"),
    ]

    KIND_CHOICES = [
        ("강아지", "Dog"),
        ("고양이", "Cat"),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    kind = forms.ChoiceField(choices=KIND_CHOICES, widget=forms.RadioSelect)
    image = forms.ImageField(required=False)
    video = forms.FileField(required=False)

    class Meta:
        model = Post  # 사용할 모델
        fields = ["kind", "category", "title", "content", "image", "video"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 10}),
        }
