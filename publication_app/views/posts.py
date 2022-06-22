from django.views import View
from publication_app.forms.posts import AddImagePost
from django.shortcuts import render, redirect
from publication_app.models import Media


class PostCreate(View):

    def get(self, request):

            form = AddImagePost()
            return render(request, 'post_create_form.html', context={
                'title': 'New Post',
                'form': form
            })


    def post(self,request):

        bound_form = AddImagePost(request.POST, request.FILES)
        files = request.FILES.getlist('image')

        if len(files) > 4:
            return render(request, 'post_create_form.html', context={
                'title': 'New Post',
                'form': bound_form,
                'error': 'Image upload error: Allowed upload limit is no more than 4 files!'
            })

        if bound_form.is_valid():
            post_object = bound_form.save(commit=False)
            post_object.user = request.user
            post_object.save()
            for f in files:
                Media.objects.create(post=post_object,image_post=f)
            return redirect('main_page')
        return render(request, 'main_page.html', context={
            'title': 'New Post',
            'form': bound_form
        })