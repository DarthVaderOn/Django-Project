from django.shortcuts import redirect, render
from django.views import View
from publication_app.forms.registration import RegistrationForm

class RegistrationView(View):
    def get(self, request):
        reg_form = RegistrationForm()
        contex = {
            'reg_form': reg_form,
        }
        return render(request, 'registration_page.html', contex)

    def post(self, request):
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('/authorization')
        contex = {
            'reg_form': reg_form,
        }
        return render(request, 'registration_page.html', contex)