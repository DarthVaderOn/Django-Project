from django.shortcuts import render
from django.views import View
from media_app.models import Media
from media_app.models import Post
from tags_app.models import Tag


class MainPageView(View):
    def get(self, request):
        posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()
        tag = Tag.objects.all()
        image_post = Media.objects.all()
        contex = {'title': 'Hello World',
                  'posts': posts,
                  'image_post': image_post,
                  'tag': tag
                  }
        return render(request, 'main_page.html', contex)


    def get_tags(request, tag_id):
        posts = Post.objects.filter(tag_id=tag_id)
        tag = Tag.objects.all()
        tags = Tag.objects.get(pk=tag_id)
        return render(request, 'tag.html', {
            'posts': posts,
            'tag': tag,
            'tags': tags

        })