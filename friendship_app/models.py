from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class FriendshipRequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='friendship_request')
    user_invite = models.ForeignKey(User,on_delete=models.CASCADE, related_name='friendship')
    friendship_result = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"User #{self.user_id} and user #{self.user_invite_id} friendship requested: {self.friendship_result}"


class FollowRequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='follow_request')
    user_follow = models.ForeignKey(User,on_delete=models.CASCADE, related_name='follow')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"User #{self.user_id} follows #{self.user_follow_id}"