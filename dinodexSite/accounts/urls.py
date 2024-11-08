from django.urls import path, include

from .views import userSuccess, userRegistro, userLogin, userLogout, userMenuPerfiles

urlpatterns = [
    path('success/', userSuccess, name="userSuccess"),
    path('login/', userLogin, name="userLogin"),
    path('logout/', userLogout, name="userLogout"),
    path('registro/', userRegistro, name="userRegistro"),
    path('perfil/', userMenuPerfiles, name="userMenuPerfiles"),
]
