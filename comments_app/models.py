from django.db import models
from publication_app.models import Post
from profile_app.models import User


# Create your models here.


class Comments(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=False, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')