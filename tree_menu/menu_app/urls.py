from django.urls import path

from menu_app import views


app_name = "menu_app"

urlpatterns = [
    path('', views.MenuView.as_view(), name="main_menu"),
    path('<str:menu_name>/', views.MenuView.as_view(), name="menu_view"),
]
