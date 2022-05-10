from django.shortcuts import render
from django.views import View

from publication_app.models import Post


class MainPageView(View):
    def get(self, request):
        posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()
        contex = {'title': 'Hello World', 'posts': posts}
        return render(request, 'main_page.html', contex)