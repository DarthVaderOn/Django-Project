from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from publication_app.forms.authorization import LoginForm
from publication_app.models import Post


class Authorization_page(View):
    def get(self,request):
        form = LoginForm()
        contex = {
            'form': form,
        }
        return render(request, 'authorization_page.html', contex)

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Аутентификации прошла успешно!')
            else:
                return HttpResponse('Ошибка аутентификации!')
            contex = {
                'form': form,
            }
            return render(request, 'authorization_page.html', contex)