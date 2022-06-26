from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from django.views import View
from publication_app.models import Media
from publication_app.models import Post
from tags_app.models import Tag


class MyPosts(View):

    def get(self, request):

        user_id = User.objects.filter(profile=request.user.profile.pk)

        user_post = []

        for user in user_id:

            if user.pk not in user_post:
                user_post.append(user.pk)

        if user_id:

                posts = Post.objects.filter(is_public=True).filter(user_id__in=user_post).all()
                tag = Tag.objects.annotate(count=Count("post")).order_by("-count")[:5]
                image_post = Media.objects.all()
                if posts:
                    contex = {'title': 'My Posts!',
                              'posts': posts,
                              'image_post': image_post,
                              'tag': tag,
                              }
                else: contex = {'title': 'My Posts!',
                      }
        else:
            contex = {'title': 'My Posts!',
                      }
        return render(request, 'my_posts.html', contex)


    def get_tags(request, tag_id):

        posts = Post.objects.filter(is_public=True).all()
        tag = Tag.objects.annotate(count=Count("post")).order_by("-count")[:5]
        image_post = Media.objects.all()
        tags = Tag.objects.get(pk=tag_id)
        return render(request, 'tag.html', {
            'title': 'Categories',
            'posts': posts,
            'image_post': image_post,
            'tag': tag,
            'tags': tags,
        })