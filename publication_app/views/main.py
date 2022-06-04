from django.db.models import Count
from django.shortcuts import render
from django.views import View
from publication_app.models import Media
from publication_app.models import Post
from tags_app.models import Tag


class MainPageView(View):
    def get(self, request):
        posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()
        tag = Tag.objects.annotate(count=Count("post")).order_by("-count")[:5]
        image_post = Media.objects.all()
        contex = {'title': 'Hello World',
                  'posts': posts,
                  'image_post': image_post,
                  'tag': tag
                  }
        return render(request, 'main_page.html', contex)


    def get_tags(request, tag_id):
        posts = Post.objects.filter(tag_id=tag_id).order_by('-id').all()
        tag = Tag.objects.annotate(count=Count("post")).order_by("-count")[:5]
        image_post = Media.objects.all()
        tags = Tag.objects.get(pk=tag_id)
        return render(request, 'tag.html', {
            'title': 'Category',
            'posts': posts,
            'image_post': image_post,
            'tag': tag,
            'tags': tags,
        })