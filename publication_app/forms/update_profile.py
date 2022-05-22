from django.contrib.auth.models import User
from django import forms

from publication_app.models import Profile


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["last_name", "first_name", "email",]


class UpdateProForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "phone",]