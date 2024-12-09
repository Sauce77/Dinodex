from django.contrib import admin

# Register your models here.
from .models import Mensaje, Foro
admin.site.register(Mensaje)
admin.site.register(Foro)
