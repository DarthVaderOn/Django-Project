from django.shortcuts import render
from .models import Post

# Create your views here.
def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()
    contex = {'title': 'Hello World', 'posts': posts }
    return render(request, 'main_page.html', contex)
