from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("password_update/", views.password_update, name="password_update"),
    path("user_update/", views.user_update, name="user_update"),
    path("product/<int:pk>", views.product, name="product"),
    path("category/<str:foo>", views.category, name="category"),
]
