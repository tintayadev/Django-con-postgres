from django.shortcuts import render
from cine.models import Peliculas, Clientes, Reservaciones
from django.http import JsonResponse

def lista_peliculas(request):
    peliculas = Peliculas.objects.all()
    return render(request, 'cine/lista_peliculas.html', {'peliculas': peliculas})

def mostrar_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'cine/clientes.html', {'clientes': clientes})

def mostrar_peliculas(request):
    peliculas = Peliculas.objects.all()
    return render(request, 'cine/peliculas.html', {'peliculas': peliculas})


def mostrar_reservaciones(request):
    # Obtener todas las reservaciones
    reservaciones = Reservaciones.objects.all()

    # Para cada reservación, obtener los detalles del cliente y la película asociados
    for reservacion in reservaciones:
        reservacion.cliente = Clientes.objects.get(pk=reservacion.id_cliente)
        reservacion.pelicula = Peliculas.objects.get(pk=reservacion.id_pelicula)

    # Renderizar el template con los datos de las reservaciones
    return render(request, 'cine/reservaciones.html', {'reservaciones': reservaciones})