from django.shortcuts import render
from django.views import View
from media_app.models import Media
from media_app.models import Post


class MainPageView(View):
    def get(self, request):
        posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()
        image_post = Media.objects.all()
        contex = {'title': 'Hello World',
                  'posts': posts,
                  'image_post': image_post,
                  }
        return render(request, 'main_page.html', contex)