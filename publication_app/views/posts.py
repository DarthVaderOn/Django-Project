import os
from django.core.mail import send_mail
from django.views import View
from publication_app.forms.posts import AddImagePost
from django.shortcuts import render, redirect
from publication_app.models import Media, Post
from publication_app.tasks import mailing_list_email_task
from user_app.models import User


class PostCreate(View):
    """Класс создания постов"""

    def get(self, request):
        """Представление формы"""

        form = AddImagePost()
        return render(request, 'post_create_form.html', context={
            'title': 'New Post',
            'form': form
        })


    def post(self,request):
        """Сохранение формы"""

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
            mailing_list_email_task()
            for spam in User.objects.all():
                send_mail(
                    'New Posts!',
                    'New and bright posts only on our website. https://django-darth-vader-on.herokuapp.com/',
                    str(os.getenv('EMAIL_HOST_USER')),  # Enter your email address
                    [spam.email]
                )
            for f in files:
                Media.objects.create(post=post_object,image_post=f)
            return redirect('my_post')
        return render(request, 'main_page.html', context={
            'title': 'New Post',
            'form': bound_form
        })