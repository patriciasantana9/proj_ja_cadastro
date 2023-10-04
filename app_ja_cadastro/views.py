from django.shortcuts import render
from .models import Cadastrado

# Create your views here.
def home(request):
   return render(request,'cadastrados/home.html')

def listagem(request):
   #salvar os dados da tela no banco de dados
   novo_gasto = Cadastrado()

   novo_gasto.gas = request.POST.get('gas')
   novo_gasto.energia = request.POST.get('energia')
   novo_gasto.agua = request.POST.get('agua')
   novo_gasto.comida = request.POST.get('comida')
   novo_gasto.aluguel = request.POST.get('aluguel')
   novo_gasto.outros = request.POST.get('outros')

   novo_gasto.save()

   #exibir os gastos cadastrados em uma nova página
   cadastrados = {
      'cadastrados': Cadastrado.objects.all()
   }

   #retornar os dados para a página de listagem de dados
   return render(request,'cadastrados/cadastrados.html',cadastrados)