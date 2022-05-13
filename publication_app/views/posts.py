from django.views import View
from publication_app.forms.posts import PostForm
from django.shortcuts import render, redirect


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'post_create_form.html', context={'form': form})

    def post(self,request):
        bound_form = PostForm(request.POST, request.FILES)
        if bound_form.is_valid():
            print(request.POST)
            print(request.FILES)
            bound_form.save()
            return redirect('main_page')
        return render(request, 'main_page.html', context={'form': bound_form})