from django.db import models, transaction


class Saldo_geral(models.Model):
    saldo_geral = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return str(self.saldo_geral)
     
class Conta(models.Model):
    """Representa as contas que o usuario vai possuir e o seu objetivo"""
    conta = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=500)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.conta

class Movimento(models.Model):
    TIPO_MOVIMENTO = (
        ('Deposito', 'DEPOSITO'),
        ('Levantamento', 'LEVANTAMENTO')
    )
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='movimentos')
    tipo = models.CharField(max_length=12, choices=TIPO_MOVIMENTO, default='DEPOSITO')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=50, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.tipo == 'DEPOSITO':
                self.conta.saldo += self.valor

            elif self.tipo == 'LEVANTAMENTO':
                if self.conta.saldo < self.valor:
                    raise('Saldo insuficiente')
                
                self.conta.saldo -= self.valor

            self.conta.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.conta} {self.valor} {self.tipo}'
