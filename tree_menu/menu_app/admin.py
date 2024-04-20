from django.contrib import admin
from menu_app.models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    ordering = ["name"]
    search_fields = ["name", "url", "named_url"]
    list_display = ["name", "parent", "url", "named_url"]
    list_filter = ["name"]
