from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    NimOrNip = forms.CharField(max_length=100, label='Nim/Nip')
    password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        cleaned_data = super().clean()
        NimOrNip = cleaned_data.get('NimOrNip')
        password = cleaned_data.get('password')
        user = authenticate(NimOrNip=NimOrNip, password=password)
        if user is None:
            raise forms.ValidationError('Invalid email or password.')
        cleaned_data['user'] = user
        return cleaned_data
