from django.views.generic import TemplateView


class MenuView(TemplateView):
    template_name = "menu_app/index.html"