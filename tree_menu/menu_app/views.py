from typing import Any
from django.views.generic import TemplateView


class MenuView(TemplateView):
    template_name = "menu_app/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        menu_name = self.kwargs.get("menu_name")
        context["menu_name"] = menu_name
        return context
