from django.db import models
from user_app.models import User
from media_app.models import MediaFile
from tags_app.models import Tag


# Create your models here.


class Post(models.Model):
    """Модель постов"""
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    is_public = models.BooleanField(default=True)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, verbose_name='Tags')
    file = models.ForeignKey(MediaFile, on_delete=models.SET_NULL, null=True, blank=True)


class Media(models.Model):
    """Модель изображений в постах"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_post = models.ImageField(null=False, blank=True)