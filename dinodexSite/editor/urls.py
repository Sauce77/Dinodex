from django.urls import path, include

from .views import editorInicio, editorCatalogo, editorEditaDino

urlpatterns = [
    path('inicio/', editorInicio, name="editorInicio"),
    path('catalogo/', editorCatalogo, name="editorCatalogo"),
    path('editar/', editorEditaDino, name="editorEditaDino"),
]
