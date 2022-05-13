from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at',)
    ordering = ('-created_at', '-id',)
    readonly_fields = ('created_at',)