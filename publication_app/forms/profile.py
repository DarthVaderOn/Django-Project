from django import forms
from django.views.generic import UpdateView


class UpdateProfileForm(UpdateView):
    model = User
    template_name = "update_profile.html"
    fields = ["last_name", "first_name", "email"]
