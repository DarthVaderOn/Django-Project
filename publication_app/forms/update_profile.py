from django.contrib.auth.models import User
from django import forms

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["last_name", "first_name", "email"]