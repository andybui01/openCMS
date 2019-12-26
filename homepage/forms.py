from django import forms

class LoginForm(forms.Form):
    username = forms.EmailField(label='Email', required=True)
    password = forms.CharField(widget=forms.PasswordInput)

class MeetForm(forms.Form):
    meet_id = forms.IntegerField(label='Meet Number', required=True)