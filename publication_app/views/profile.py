from django.shortcuts import render
from django.views import View


class Profile_User(View):
    def get(self, request):
        return render(request, "profile.html")