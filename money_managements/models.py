from django.db import models

class Conta(models.Model):
    """Representa as contas que o usuario vai possuir e o seu objetivo"""
    conta = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500)
    saldo = models.BigIntegerField(default=0)

    def __str__(self):
        return self.conta
    
class Deposito(models.Model):
    """Entradas de valores afeta apenas a conta selecionada"""
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    valor = models.BigIntegerField()
    data = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    descricao = models.CharField(50)

    def __str__(self):
        return self.descricao

class Levantamento(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    valor = models.BigIntegerField()
    data = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)

class Movimento(models.Model):
    conta = models.CharField(max_length=100)
    valor = models.BigIntegerField()
    data = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)