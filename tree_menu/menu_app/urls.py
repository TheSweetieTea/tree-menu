from django.urls import path

from menu_app import views

urlpatterns = [
    path('', views.MenuView.as_view(), name="menu_view")
]
