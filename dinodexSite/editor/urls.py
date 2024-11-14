from django.urls import path, include

from .views import editorInicio, editorCatalogo, editorEditarDino, editorEliminarDino, editorAgregarDino

urlpatterns = [
    path('inicio/', editorInicio, name="editorInicio"),
    path('catalogo/', editorCatalogo, name="editorCatalogo"),
    path('editar/', editorEditarDino, name="editorEditarDino"),
    path('eliminar/', editorEliminarDino, name="editorEliminarDino"),
    path('agregar/', editorAgregarDino, name="editorAgregarDino"),
]
