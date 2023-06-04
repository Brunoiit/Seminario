from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ver', views.ver, name='ver'),
    path('agregar', views.agregar, name='agregar'),
    path('modificar', views.modificar, name='modificar'),
    path('eliminar', views.eliminar, name='eliminar')
]

