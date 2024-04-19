from django.contrib import admin
from .models import Peliculas, Clientes, Reservaciones
# Register your models here.
admin.site.register(Peliculas)
admin.site.register(Clientes)
admin.site.register(Reservaciones)