from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('menu/', views.menu, name="menu"),
    path('blog/', views.blog, name="blog"),
    path('listas/', views.listas, name="listas"),
]
