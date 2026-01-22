from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from decimal import Decimal
from .models import Conta, Movimento


# Create your views here.
def index(request):
    movimentos = Movimento.objects.all().order_by('data')
    dados = {'movimentos' : movimentos[:10]}
    return render(request, 'm_mg/index.html', dados)

def contas(request):
    contas = Conta.objects.all()
    dados = { 'contas' : contas }
    return render(request, 'm_mg/contas.html', dados)

def conta(request, conta_id):
    conta = Conta.objects.get(id=conta_id)
    movimentos = conta.movimentos.all().order_by('data')
    dados = { 'conta' : conta, 'movimentos' : movimentos[:10] }
    return render(request, 'm_mg/conta.html', dados)

def nova_conta(request):
    if request.method != 'POST':
        p = 1
    else:
        conta = Conta()
        conta.conta = request.POST.get('conta')
        conta.descricao = request.POST.get('descricao')
        conta.saldo = request.POST.get('saldo')
        conta.save()
        return HttpResponseRedirect(reverse('contas'))
    
    return render(request, 'm_mg/nova_conta.html')

def movimento(request, conta_id):
    conta = Conta.objects.get(id=conta_id)

    if request.method != 'POST':
        pass

    else:
        Movimento.objects.create(
            conta= conta,
            valor= Decimal(request.POST['valor']),
            tipo= request.POST['tipo'],
            descricao= request.POST['descricao'],
        )
        return HttpResponseRedirect(reverse('conta', args=[conta.id]))
    dados = {'conta' : conta }
    return render(request, 'm_mg/movimento.html', dados)

def listar_movimentos(request, conta_id):
    conta = Conta.objects.get(id=conta_id)
    movimentos = conta.movimentos.all().order_by('data')
    dados = {'movimentos' : movimentos }
    return render(request, 'm_mg/movimentos.html', dados)
