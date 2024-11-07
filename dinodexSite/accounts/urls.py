from django.urls import path, include

from .views import userSuccess, userRegistro, userLogin, userLogout

urlpatterns = [
    path('success/', userSuccess, name="userSuccess"),
    path('registro', userRegistro, name="userRegistro"),
    path('login/', userLogin, name="userLogin"),
    path('logout/', userLogout, name="userLogout"),
]
