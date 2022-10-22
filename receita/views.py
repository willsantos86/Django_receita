from django.shortcuts import render

def index(request):
    receitas = {
        1: 'lasanha',
        2: 'Sopa de legumes',
        3: 'Sorvete',
        4: 'Bolo de Chocolate'
    }

    dados = {
        'nome_das_receitas': receitas
    }

    return render(request,'index.html',dados)


def receita(request):
    return render(request, 'receita.html')

