from django.conf.urls import url
from . import views

urlpatterns = [

    # wining/register
    url(r'^$', views.register, name="register"),
    # winning/login
    url(r'^login/$', views.loginPage, name="login"),
    # winning/logOut
    url(r'^logout/$', views.logOutUser, name="logout"),

    # wining/index
    url(r'^home/$', views.homePage, name="home"),
]