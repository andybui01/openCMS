from django import forms

class SessionForm(forms.Form):
    bodyweight = forms.IntegerField(
        label="Bodyweight:",
        required=True)
    letter = forms.CharField(
        label="Letter:",
        max_length=1,
        required=True)
    start_time = forms.TimeField(
        label="Start Time:",
        required=True,
        help_text="HH:MM")