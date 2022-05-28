from django.contrib import admin
from tags_app.models import Tags


# Register your models here.


@admin.register(Tags)
class Tag(admin.ModelAdmin):
    list_display = ('tag', 'id')