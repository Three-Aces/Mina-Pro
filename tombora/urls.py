from django.urls import path
from . import views

app_name = 'tombora'

urlpatterns = [

    path('', views.homePage, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logOutUser, name="logout"),

]