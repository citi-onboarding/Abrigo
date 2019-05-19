from django.db import models

# Create your models here.

#Model Bancos

class Contas(models.Model):
    foto = models.ImageField(upload_to='contas_image/')
    conta_bancaria = models.IntegerField(max_length=10, blank=False, null=True)
    numero_agencia = models.IntegerField(max_length=10, blank=False, null=True)
    nome_titular = models.CharField(max_length=100, blank=False, null=True)
    codigo_banco = models.IntegerField(max_length=5, blank=False, null=True)
    cpf = models.CharField(max_length=length, blank=False, null=True)
    def __str__(self):
        return self.conta_bancaria

    class Meta:
        verbose_name = 'Contas Bancária'

#Model Doacao
class Doacao(models.Model):
	voluntario = models.CharField(max_length=100, blank=False, null=False)
	local = models.TextField(null=False, blank=False)
	dias = models.CharField(max_lenght=50 null=True, blank=True)
	horario = models.IntegerField(null=True, blank=True)
	foto = models.ImageField(upload_to="doacao_image/")

	def __str__(self):
		return self.local

	class Meta{
		verbose_name_plural = 'Pontos de arrecadação'
		verbose_name = 'Ponto de arrecadação'
	}
#Model Eventos