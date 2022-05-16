from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    is_public = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(blank=True, null=True)
    phone = models.CharField(
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        max_length=17,
        blank=True,
        null=True,
    )
    about = models.TextField(max_length=4096, blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
