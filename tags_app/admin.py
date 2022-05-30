from django.contrib import admin
from tags_app.models import Tag

# Register your models here.


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ('id', 'title',)
    ordering = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
