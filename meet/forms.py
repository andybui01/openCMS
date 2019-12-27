from django import forms

class SessionForm(forms.Form):
    bodyweight = forms.IntegerField(
        label="Bodyweight:",
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': '81'}))
    letter = forms.CharField(
        label="Letter:",
        max_length=1,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'A'}))
    start_time = forms.TimeField(
        label="Start Time (HH:MM):",
        required=True,
        widget=forms.TimeInput(attrs={'placeholder': '13:00'}))