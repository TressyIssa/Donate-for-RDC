from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('tests', views.test, name="test"),
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register, name="register"),
    path('formdon', views.addDon, name="formdon"),
    path('addprojet', views.addProjet, name="addprojet"),
    path('home', views.home, name="home"),
    path('save_transaction', views.save_transaction, name="save_transaction"),
    path('update_transaction', views.update_transaction, name="update_transaction"),
]