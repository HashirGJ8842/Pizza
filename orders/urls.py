from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("login", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout_view"),
    path("register", views.register, name="register"),
    path("shop", views.shopping_list, name="shopping_list"),
    path("toppings", views.toppings, name="toppings"),
    path("final", views.final, name="final"),
]