from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/<str:nome>/', views.pokemon_banco, name='pokemon'),
    path('tipo/<str:nome>/', views.tipos, name='tipos'),
]