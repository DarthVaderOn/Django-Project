from django.views import View
from publication_app.forms.posts import AddImagePost
from django.shortcuts import render, redirect
from publication_app.models import Post, ImagePost


class PostCreate(View):
        def get(self, request):
            if request.user.is_authenticated:
                form = AddImagePost()
                return render(request, 'post_create_form.html', context={'form': form})
            return redirect("auth_page")

        def post(self,request):
            bound_form = AddImagePost(request.POST, request.FILES)
            files = request.FILES.getlist('image')
            if bound_form.is_valid():
                print(request.POST)
                print(request.FILES)
                title = bound_form.cleaned_data['title']
                text = bound_form.cleaned_data['text']
                is_public = bound_form.cleaned_data['is_public']
                post_object = Post.objects.create(title=title, text=text, is_public=is_public)
                for f in files:
                    ImagePost.objects.create(post=post_object,image_post=f)
                return redirect('main_page')
            return render(request, 'main_page.html', context={'form': bound_form})
