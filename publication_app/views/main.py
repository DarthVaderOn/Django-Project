from django.db.models import Count
from django.shortcuts import render
from django.views import View
from friendship_app.models import FollowRequest
from publication_app.models import Media
from publication_app.models import Post
from tags_app.models import Tag


class MainPageView(View):

    def get(self, request):
        subscriber = FollowRequest.objects.filter(user=request.user.pk)

        users_follow = []

        for users in subscriber:

            if users.user_follow.pk not in users_follow:
                users_follow.append(users.user_follow.pk)

        if subscriber:

                posts = Post.objects.filter(is_public=True).filter(user_id__in=users_follow).all()
                tag = Tag.objects.annotate(count=Count("post")).order_by("-count")[:5]
                image_post = Media.objects.all()
                if posts:
                    contex = {'title': 'Hello World!',
                              'posts': posts,
                              'image_post': image_post,
                              'tag': tag,
                              }
        else:
            contex = {'title': 'Hello World!',
                      }
        return render(request, 'main_page.html', contex)


    def get_tags(request, tag_id):

        subscriber = FollowRequest.objects.filter(user=request.user.pk)

        users_follow = []

        for users in subscriber:

            if users.user_follow.pk not in users_follow:
                users_follow.append(users.user_follow.pk)

        if subscriber:

                posts = Post.objects.filter(tag_id=tag_id).order_by('-id').filter(user_id__in=users_follow).all()
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
        else:
            contex = {'title': 'Hello World!',
                      }
        return render(request, 'main_page.html', contex)