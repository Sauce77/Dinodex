from django.urls import path, include

from .views import userCatalogo

urlpatterns = [
    path('catalogo/', userCatalogo, name="userCatalogo"),
]
