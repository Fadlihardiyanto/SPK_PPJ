# forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import MyUser

class CustomAuthenticationForm(AuthenticationForm):
    NimOrNip = forms.CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False, 'placeholder': 'Email'})

    def clean(self):
        cleaned_data = super().clean()
        NimOrNip = cleaned_data.get('NimOrNip')
        email = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if email and password and NimOrNip:
            try:
                user = MyUser.objects.get(email=email, NimOrNip=NimOrNip)
            except MyUser.DoesNotExist:
                raise forms.ValidationError("Invalid login credentials.")
            else:
                if not user.check_password(password):
                    raise forms.ValidationError("Invalid login credentials.")
                cleaned_data['user'] = user
        else:
            raise forms.ValidationError("Please enter your email, NIM/NIP, and password.")

        return cleaned_data


class RegistrationAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = MyUser
        fields = ['email', 'name', 'NimOrNip', 'is_staff']
        labels = {'is_staff': 'Admin', 'NimOrNip': 'NIM/NIP'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['password'].required = False
            self.fields['confirm_password'].required = False

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password or confirm_password:
            if password != confirm_password:
                raise forms.ValidationError('Passwords do not match.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
