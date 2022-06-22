from django.shortcuts import render, redirect
from profile_app.forms.update_profile import UpdateProfileForm, UpdateProForm
from profile_app.models import Profile


def user_redaction(request):

    if request.method == 'POST':
        user_form = UpdateProfileForm(instance=request.user, data=request.POST)
        profile_form = UpdateProForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/profile')
    else:
        user_form = UpdateProfileForm(instance=request.user)
        profile_form = UpdateProForm(instance=request.user.profile)
        image = Profile.objects.get(pk=request.user.pk)
        return render(request,'update_profile.html', {'user_form': user_form,
                                                      'profile_form': profile_form,
                                                      'image': image
                                                      })