from django.contrib import admin
from friendship_app.models import FriendshipRequest, FollowRequest


# Register your models here.



@admin.register(FriendshipRequest)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_invite', 'friendship_result', 'created_at')
    list_editable = ('friendship_result',)
    search_fields = ('user__username', 'user_invite__username')


@admin.register(FollowRequest)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_follow', 'follow_result', 'created_at')
    list_editable = ('follow_result',)
    search_fields = ('user__username', 'user_follow__username')