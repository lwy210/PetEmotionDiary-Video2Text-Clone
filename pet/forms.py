from django import forms

from pet.models import Personality, Pet


class PetForm(forms.ModelForm):
    KIND_CHOICES = [
        ("Dog", "강아지"),
        ("Cat", "고양이"),
    ]
    GENDER_CHOICES = [
        ("W", "암컷"),
        ("M", "수컷"),
    ]
    image = forms.ImageField(required=False)
    kind = forms.ChoiceField(choices=KIND_CHOICES, widget=forms.RadioSelect)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)

    activity = forms.ChoiceField(
        choices=Personality.ACTIVITY_CHOICES, widget=forms.RadioSelect, required=False
    )
    relationship = forms.ChoiceField(
        choices=Personality.RELATIONSHIP_CHOICES,
        widget=forms.RadioSelect,
        required=False,
    )
    proto_dog = forms.ChoiceField(
        choices=Personality.PROTO_DOG_CHOICES, widget=forms.RadioSelect, required=False
    )
    dependence = forms.ChoiceField(
        choices=Personality.DEPENDENCE_CHOICES, widget=forms.RadioSelect, required=False
    )

    class Meta:
        model = Pet
        fields = [
            "gender",
            "owner_name",
            "birth_day",
            "meet_day",
            "name",
            "kind",
            "image",
            "is_neutered",
            "activity",
            "relationship",
            "proto_dog",
            "dependence",
        ]
        widgets = {
            "birth_day": forms.DateInput(attrs={"type": "date"}),
            "meet_day": forms.DateInput(attrs={"type": "date"}),
            "is_neutered": forms.CheckboxInput(),
        }
