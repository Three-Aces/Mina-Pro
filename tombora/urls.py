from django.urls import path
from . import views

urlpatterns = [

    path('', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logOutUser, name="logout"),
    path('home/', views.homePage, name="home"),
]