from django import forms

class SessionForm(forms.Form):
    bodyweight = forms.IntegerField(label="Bodyweight:",required=True,widget=forms.NumberInput(attrs={'placeholder': '81'}))
    letter = forms.CharField(label="Letter:", max_length=1, required=True)
    start_time = forms.TimeField(label="Start Time:", required=True)