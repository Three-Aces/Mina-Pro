from django.urls import path
from .import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', views.dashboardPage, name='dashboard'),
    path('blank/', views.blankPage, name='blank'),
    path('login/', views.loginPage, name='login'),
    path('chart/', views.chartPage, name='chart'),
]