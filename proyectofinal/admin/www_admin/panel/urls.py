from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('cerrarSesion/', views.cerrarSesion, name="cerrarSesion"),
    path('', views.index, name='index'),
    path('ver', views.ver, name='ver'),
    path('agregar', views.agregar, name='agregar'),
    path('publicar', views.publicar, name='publicar'),
    path('modificar/<int:id_usr>/', views.modificar, name='modificar'),
    path('publicacion/<int:id_pblc>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('guardar_comentario/', views.guardar_comentario, name='guardar_comentario'),
    path('calculadora/', views.calculadora, name='calculadora'),
    # path('eliminar/<int:id_usr>/', views.eliminar, name='eliminar')
]