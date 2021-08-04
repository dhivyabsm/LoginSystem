from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.loginPage, name="login"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout_view, name="logout"),
    path("home", views.home, name="home"),
]
