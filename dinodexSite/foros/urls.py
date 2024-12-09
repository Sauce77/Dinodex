from django.urls import path, include

from .views import forosInicio, userAgregarMensaje, userMostrarForo, adminCrearForo, adminMostrarCodigo

urlpatterns = [
    path('inicio/', forosInicio, name="forosInicio"),
    path('foro/', userMostrarForo, name="userMostrarForo"),
    path('mensaje/', userAgregarMensaje, name="userAgregarMensaje"),
    path('crear/', adminCrearForo, name="adminCrearForo"),
    path('codigo/', adminMostrarCodigo, name="adminMostrarCodigo"),
]
