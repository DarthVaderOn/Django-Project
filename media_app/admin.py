from django.contrib import admin
from django.utils.safestring import mark_safe
from media_app.models import Media, Post


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_public',)
    ordering = ('-created_at', '-id',)
    readonly_fields = ('created_at',)
    list_editable = ('is_public',)


@admin.register(Media)
class MenuItemAdmin(admin.ModelAdmin):
    model = Media
    max_num = 4
    list_display = ('image_post','preview')
    readonly_fields = ('image_post','preview')


    def preview(self, obj):
        if obj.image_post:
            return mark_safe(
                f'<a target=_blank href={obj.image_post.url}>'
                f'<img src={obj.image_post.url} width="100" height="100">'
                f'</a>'
            )