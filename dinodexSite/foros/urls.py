from django.urls import path, include

from .views import forosInicio

urlpatterns = [
    path('inicio/', forosInicio, name="forosInicio"),
]
