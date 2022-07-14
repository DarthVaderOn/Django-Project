from user_app.models import User
from django import forms


class RegistrationForm(forms.ModelForm):
    """Класс формы регистрации пользователя"""

    email = forms.EmailInput()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        """Вывод полей при регистрации"""
        model = User
        fields = ('username', 'email', 'password',)


    def save(self, commit=True):
        """Сохраняем нового пользователя и хешируем пароль"""
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user