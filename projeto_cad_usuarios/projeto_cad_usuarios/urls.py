
from django.urls import path
from app_cad_usuarios import views # importar da aplicação

urlpatterns = [
    # rota, view responsáve,  nome de referência
    # usuarios.com
    path('',views.home,name='home'),

    # usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
