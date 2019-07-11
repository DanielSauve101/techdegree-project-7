from django import forms

from . import models


class ProfileForm(forms.ModelForm):
    verify_email = forms.EmailField(label="Verify email:")
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
                "Both email fields are required to match.")
