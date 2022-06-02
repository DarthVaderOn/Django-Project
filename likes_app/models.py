from django.db import models
from comments_app.models import Comments
from media_app.models import Post
from profile_app.models import User


# Create your models here.


class LikePost(models.Model):
    like_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class LikeComment(models.Model):
    like_comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)