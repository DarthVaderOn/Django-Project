from django.contrib.auth.models import User
from django import forms


class RegistrationForm(forms.ModelForm):
    email = forms.EmailInput()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user