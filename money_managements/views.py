from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Conta


# Create your views here.
def index(request):
    return render(request, 'm_mg/index.html')

def contas(request):
    contas = Conta.objects.all()
    dados = { 'contas' : contas }
    return render(request, 'm_mg/contas.html', dados)

def conta(request, conta_id):
    conta = Conta.objects.get(id=conta_id)
    dados = { 'conta' : conta }
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