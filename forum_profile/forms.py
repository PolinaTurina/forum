from django import forms
from forum_profile.models import Profile


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        field = '__all__'