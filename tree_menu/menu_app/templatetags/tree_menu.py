from django import template
from django.utils.safestring import mark_safe
from django.db.models.query import QuerySet
from menu_app.models import MenuItem

register = template.Library()


@register.simple_tag()
def draw_menu(menu_name: str):
    menu_items = (
            MenuItem.objects.
            filter(name=menu_name).
            select_related("parent")
        )

    return mark_safe(render_menu(menu_items))


def render_menu(menu_items: QuerySet[MenuItem]):
    result_html = "<ul>"

    for item in menu_items:
        result_html += "<li>"
        if item.url:
            result_html += f"<a href='{item.url}'>{item.name}</a>"
        elif item.named_url:
            result_html += f"<a href='{item.named_url}'>{item.name}</a>"
        else:
            result_html += item.name

        if item.children.exists():
            result_html += render_menu(item.children.all())

        result_html += "</li>"

    result_html += "</ul>"
    return result_html
