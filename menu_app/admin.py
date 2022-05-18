from django.contrib import admin
from menu_app.models import Menu, MenuItem


# Register your models here.


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    model = Menu


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    model = MenuItem