from django import forms

class MeetForm(forms.Form):
    meet_id = forms.IntegerField(label='Meet Number', required=True)