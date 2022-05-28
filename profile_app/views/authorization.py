from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth

from profile_app.forms.authorization import LoginForm



class Authorization(View):
    @staticmethod
    def get(request):
        form = LoginForm()
        contex = {
            'auth_form': form,
        }
        return render(request, 'authorization_page.html', contex)

    @staticmethod
    def post(request):
        form = LoginForm(request.POST)
        error = False

        if form.is_valid():
            user = auth.authenticate(request, **form.cleaned_data)

            if user is not None:
                auth.login(request, user)

                next_page =request.GET.get('next', '/')
                return redirect(next_page)

            error = True

        contex = {
            'title': 'Authorization',
            'auth_form': form,
            'error': error,
        }
        return render(request, 'authorization_page.html', contex)