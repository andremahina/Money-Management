from .models import Saldo_geral, Conta

def dados_globais(request):
    saldo_geral = Saldo_geral()
    contas = Conta.objects.all()
    saldo = 0
    for conta in contas:
        saldo += conta.saldo
    saldo_geral.saldo_geral = saldo

    dados = { 'saldo_geral' : str(saldo_geral) +'KZ' }
    return dados
