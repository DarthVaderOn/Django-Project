from django.contrib import admin
from django.utils.safestring import mark_safe
from messenger_app.models import Messenger


# Register your models here.


@admin.register(Messenger)
class MessengerAdmin(admin.ModelAdmin):
    """Вывод полей чата в админке"""
    list_display = ('id', 'sender', 'recipient', 'created_at', 'text', 'preview',)
    ordering = ('-created_at', '-id',)
    readonly_fields = ('created_at', 'preview')
    search_fields = ('sender__username', 'recipient__username')


    def preview(self, obj):
        """Превью картинок в чате админки"""
        if obj.file:
            return mark_safe(
                f'<a target=_blank href={obj.file.file.url}>'
                f'<img src={obj.file.file.url} width="100" height="100">'
                f'</a>'
            )
        else:
            return 'No Image'