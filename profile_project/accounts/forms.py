from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from . import models


class ProfileForm(forms.ModelForm):
    verify_email = forms.EmailField(label='Verify email: ')
    bio = forms.CharField(widget=forms.Textarea(attrs={'id': 'mytextarea'}), min_length=10)

    class Meta:
        model = models.Profile
        fields = [
            'first_name',
            'last_name',
            'email',
            'verify_email',
            'date_of_birth',
            'bio',
            'avatar'
        ]
        widgets = {'date_of_birth': forms.DateInput(attrs={'id': 'datepicker'})}

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify_email')

        if email != verify:
            raise forms.ValidationError(
                'Both email fields are required to match.')


class NewPasswordForm(PasswordChangeForm):
    def clean_new_password1(self):
        new_password = self.cleaned_data.get('new_password1')
        print('New password:', new_password)

        if (self.user.profile.first_name.lower() in new_password.lower()
                or self.user.profile.last_name.lower() in new_password.lower()
                or self.user.username.lower() in new_password.lower()):
            raise forms.ValidationError(
                'New password cannot contain the user name or parts of the ' +
                'user’s full name, such as their first or last name.'
            )
        return new_password
