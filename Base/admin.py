from django.contrib import admin
from .models import Laboratorio, Laboratorio, Linea_de_Investigacion, Eventos, Blog, Contacto
# Register your models here.

admin.site.register(Laboratorio)
admin.site.register(Linea_de_Investigacion)
admin.site.register(Eventos)
admin.site.register(Blog)
admin.site.register(Contacto)