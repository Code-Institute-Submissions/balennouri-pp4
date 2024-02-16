from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("addproduct/", views.addProduct, name="addproduct"),
    path("checkout/", views.checkout_views, name="checkout"),
    path("category/<str:foo>", views.category, name="category"),
    path("deleteproduct/<int:pk>", views.deleteProduct, name="deleteproduct"),
    path("info/", views.about, name="about"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("product/<int:pk>/add-comment", views.AddComments, name="add-comment"),
    path("product/<int:pk>/delete-comment", views.DeleteComments, name="delete-comment"),
    path("product/<int:pk>", views.product, name="product"),
    path("password_update/", views.password_update, name="password_update"),
    path("updateproduct/<int:pk>", views.updateProduct, name="updateproduct"),
    path("user_update/", views.user_update, name="user_update"),
    path("user_delete/", views.deleteUser, name="userdelete"),
    path("register/", views.register_user, name="register"),
    path("staff", views.StaffAdmin, name="staff"),
]
