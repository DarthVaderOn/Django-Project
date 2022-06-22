import os
from pathlib import Path
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from dotenv import load_dotenv
from profile_app.forms.registration import RegistrationForm
from profile_app.tasks import send_email_task
from django.contrib.auth import login


class RegistrationView(View):

    def get(self, request):
        reg_form = RegistrationForm()
        contex = {
            'title': 'Registration',
            'reg_form': reg_form,
        }
        return render(request, 'registration_page.html', contex)


    load_dotenv()
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)


    def post(self, request):
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            user=reg_form.save()
            send_email_task()
            send_mail('Welcome New User!',
                'This is proof the task worked!',
                str(os.getenv('EMAIL_HOST_USER')),        # Enter your email address
                [user.email])                             # Enter them email address
            user.is_active = True
            user.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('/')
        contex = {
            'title': 'Registration',
            'reg_form': reg_form,
        }
        return render(request, 'registration_page.html', contex)