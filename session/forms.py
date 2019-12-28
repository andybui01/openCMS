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

    