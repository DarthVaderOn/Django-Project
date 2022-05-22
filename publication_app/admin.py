from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from .models import Post, Profile, ImagePost


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at','is_public')
    ordering = ('-created_at', '-id',)
    readonly_fields = ('created_at',)
    list_editable = ('is_public',)


admin.site.unregister(User)


class ProfileInline(admin.StackedInline):
    model = Profile

@admin.register(User)
class UserAdmin(UserAdminBase):
    inlines = (
        ProfileInline,
    )


@admin.register(ImagePost)
class MenuItemAdmin(admin.ModelAdmin):
    model = ImagePost
    list_display = ("image_post",)
    readonly_fields = ("image_post",)
#
# def get_image(self,objects):
#     if objects.image:
#         return mark_safe(f"<a href={objects.image}>"
#                          f"<img src={objects.image} width='350' height='350'>"
#                          f"</a>")
