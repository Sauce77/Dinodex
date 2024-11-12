from django.urls import path, include

from .views import editorInicio, editorCatalogo

urlpatterns = [
    path('inicio/', editorInicio, name="editorInicio"),
    path('catalogo/', editorCatalogo, name="editorCatalogo")
]
