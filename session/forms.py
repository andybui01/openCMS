from django import forms

class CreateAthleteForm(forms.Form):
    GENDER_CHOICES = (
        (True, "Male"),
        (False, "Female"))

    name = forms.CharField(
        label="Name:",
        max_length=50,
        required=True)

    date_of_birth = forms.DateField(
        label="Date Of Birth:",
        required=True,
        help_text="YYYY-MM-DD")

    gender = forms.ChoiceField(
        label="Gender",
        choices=GENDER_CHOICES,
        required=True)

    bodyweight = forms.FloatField(
        label="Bodyweight:",
        required=True)

    affiliation = forms.CharField(
        label="Affiliation:",
        max_length=3,
        required=True,
        help_text="Max 3 letters")

class UpdateAthleteForm(forms.Form):
    # ATTEMPT_CHOICES = (
    #     (1, "SN1"),
    #     (2, "SN2"),
    #     (3, "SN3"),
    #     (4, "CJ1"),
    #     (5, "CJ2"),
    #     (6, "CJ3")
    # )
    # attempt = forms.ChoiceField(label="", help_text="", choices=ATTEMPT_CHOICES)
    weight = forms.IntegerField(label="", help_text="", required=True)
