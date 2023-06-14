from django import forms

from post.models import Post


class PostForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ("free_type", "자유게시판"),
        ("brag_type", "자랑게시판"),
        ("worry_type", "고민게시판"),
    ]

    KIND_CHOICES = [
        ("Dog", "강아지"),
        ("Cat", "고양이"),
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
