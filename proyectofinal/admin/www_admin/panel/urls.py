from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('cerrarSesion/', views.cerrarSesion, name="cerrarSesion"),
    path('', views.index, name='index'),
    path('ver', views.ver, name='ver'),
    path('agregar', views.agregar, name='agregar'),
    path('modificar/<int:id_usr>/', views.modificar, name='modificar'),
    path('eliminar/<int:id_usr>/', views.eliminar, name='eliminar')
]

