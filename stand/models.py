from django.db import models

# Create your models here.

class Stand(models.Model):
    localizacao = models.CharField(max_length=200, verbose_name='Localização do Stand')
    valor = models.FloatField(verbose_name='Preço do Stand')

    def __str__(self):
        return self.localizacao
    
class Empresa(models.Model):
    nome = models.CharField(max_length=150)
    categoria = models.CharField(max_length=150, verbose_name='Categoria da Empresa')

    def __str__(self):
        return self.nome
    
class Reserva(models.Model):
    cnpj = models.CharField(max_length=200, verbose_name='CNPJ')
    nome_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Nome da Empresa')
    quitado = models.BooleanField(verbose_name='Quitação')
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE, verbose_name='Stand')

    def __str__(self):
        return self.cnpj