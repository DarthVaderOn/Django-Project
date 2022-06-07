from django.contrib import admin
from django.utils.safestring import mark_safe
from publication_app.models import Media, Post

# Register your models here.


class MenuItemAdmin(admin.StackedInline):
    model = Media
    list_display = ('image_post','preview')
    readonly_fields = ('image_post','preview')


    def preview(self, obj):
        if obj.image_post:
            return mark_safe(
                f'<a target=_blank href={obj.image_post.url}>'
                f'<img src={obj.image_post.url} width="100" height="100">'
                f'</a>'
            )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (
        MenuItemAdmin,
    )
    list_display = ('id', 'title', 'user', 'tag', 'created_at', 'is_public',)
    ordering = ('-created_at', '-id',)
    readonly_fields = ('created_at',)
    list_editable = ('is_public', 'tag', 'user',)
    search_fields = ('title', 'text')