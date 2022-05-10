from django.shortcuts import render
from django.views import View

from publication_app.models import Post


class Profile_user(View):
    def get(self, request):
        user_ava = Profile.objects.order_by("id").all()
        user_post = Post.objects.all()

        context = {"title": "Акк", "users": user_ava, "posts": user_post,}
        return render(request, "profile.html", context)