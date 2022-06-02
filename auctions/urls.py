from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createList", views.createList, name="createList"),
    path("category", views.category, name="category"),
    path("category/<str:department>", views.listItems, name="listItems"),
    # path("seller/", views.type, name="seller"),
    path("seller/<int:itemId>", views.showItem, name="showItem"),    
    ]
