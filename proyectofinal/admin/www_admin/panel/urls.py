from django.contrib import admin
from django.urls import path
from django import views
#el . es de la misma carpeta (panel)
from . import views

#definir urlpatterns
urlpatterns = [
    path('', views.index, name="index")
]
