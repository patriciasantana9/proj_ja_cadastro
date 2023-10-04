from django.urls import path
from app_ja_cadastro import views

urlpatterns = [
    #rota, view responsável, nome de referência
    path('',views.home,name='home'),

    path('listagem/', views.listagem,name='listagem_gastos')
]
