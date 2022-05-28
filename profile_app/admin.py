from django.contrib import admin
from django.contrib.auth.models import User
from profile_app.models import Profile
from django.contrib.auth.admin import UserAdmin as UserAdminBase
# Register your models here.


admin.site.unregister(User)

class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(UserAdminBase):
    inlines = (
        ProfileInline,
    )