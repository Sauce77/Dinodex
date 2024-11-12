from django.contrib import admin

# Register your models here.
from .models import Alimentacion, Periodo, Dinosaurio

admin.site.register(Alimentacion)
admin.site.register(Periodo)
admin.site.register(Dinosaurio)
