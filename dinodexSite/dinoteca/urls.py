from django.urls import path, include

from .views import userCatalogo, userMirarDino

urlpatterns = [
    path('catalogo/', userCatalogo, name="userCatalogo"),
    path('dinosaurio/', userMirarDino, name="userMirarDino"),
]
