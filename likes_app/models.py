from django.db import models
from comments_app.models import Comments
from publication_app.models import Post
from profile_app.models import User


# Create your models here.


class LikePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='likes')

    class Meta:
        unique_together = (('post', 'user'),)


class LikeComment(models.Model):
    post_comment = models.ForeignKey(Comments, on_delete=models.CASCADE, null=False, blank=False, related_name='likes_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='likes_comment')

    class Meta:
        unique_together = (('post_comment', 'user'),)