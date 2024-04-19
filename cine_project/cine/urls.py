from django.urls import path
from . import views

urlpatterns = [
    path('lista_peliculas/', views.lista_peliculas, name='lista_peliculas'),
    path('clientes/', views.mostrar_clientes, name='mostrar_clientes'),
    path('peliculas/', views.mostrar_peliculas, name='mostrar_peliculas'),
    path('reservaciones/', views.mostrar_reservaciones, name='mostrar_reservaciones'),
]
