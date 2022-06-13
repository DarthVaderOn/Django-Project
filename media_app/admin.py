from django.contrib import admin
from django.utils.safestring import mark_safe
from media_app.models import MediaFile


# Register your models here.


@admin.register(MediaFile)
class MessengerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'file', 'uploaded_at', 'preview')
    ordering = ('-id',)
    readonly_fields = ('preview', 'file', 'uploaded_at')
    search_fields = ('user__username', 'file')


    def preview(self, obj):
        if obj.file:
            return mark_safe(
                f'<a target=_blank href={obj.file.url}>'
                f'<img src={obj.file.url} width="100" height="100">'
                f'</a>'
            )