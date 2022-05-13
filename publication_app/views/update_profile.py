from django.shortcuts import render, redirect
from django.views import View

from publication_app.forms.update_profile import UpdateProfileForm



def user_redaction(request):
    if request.method == 'POST':
        user_form = UpdateProfileForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/')
    else:
        user_form = UpdateProfileForm(instance=request.user)
        return render(request,'update_profile.html', {'user_form': user_form,})