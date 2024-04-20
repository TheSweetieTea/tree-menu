from django.contrib import admin
from menu_app.models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["name", "url", "named_url"]
