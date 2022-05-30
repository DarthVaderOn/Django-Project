from django.views import View
from media_app.forms.posts import AddImagePost
from django.shortcuts import render, redirect
from media_app.models import Media


class PostCreate(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = AddImagePost()
            return render(request, 'post_create_form.html', context={
                'title': 'New Post',
                'form': form}
                          )
        return redirect("auth_page")

    def post(self,request):
        bound_form = AddImagePost(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        if bound_form.is_valid():
            print(request.POST)
            print(request.FILES)
            post_object = bound_form.save(commit=False)
            post_object.user = request.user
            post_object.save()
            for f in files:
                Media.objects.create(post=post_object,image_post=f)
            return redirect('main_page')
        return render(request, 'main_page.html', context={
            'title': 'New Post',
            'form': bound_form}
                      )