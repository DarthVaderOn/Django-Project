from user_app.models import User
from django.db import models
from media_app.models import MediaFile


# Create your models here.


class Messenger(models.Model):
    """Модель мессенджера"""
    text = models.CharField(max_length=256, unique=False, blank=False, null=False)
    file = models.ForeignKey(MediaFile, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User,on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(User,on_delete=models.CASCADE, related_name='recipient')