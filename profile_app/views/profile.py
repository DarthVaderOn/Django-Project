from django.shortcuts import render, redirect
from django.views import View
from profile_app.models import Profile


class Profile_User(View):

    def get(self, request):
        user = Profile.objects.get(user=request.user)
        contex = {
            'title': 'Profile',
            'avatar': user,
        }
        return render(request, "profile.html", contex)