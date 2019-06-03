from django.db import models

# Create your models here.

#Model Bancos

class Contas(models.Model):
    foto = models.ImageField(upload_to='contas_image/')
    info = models.TextField(blank=False, null=False, default="Digite suas informaçoes aqui")

    def __str__(self):
        return self.info

    class Meta:
        verbose_name = 'Contas Bancária'

#Model Doacao
class Doacao(models.Model):
	voluntario = models.CharField(max_length=100, blank=False, null=False)
	local = models.CharField(max_length=250,null=False, blank=False)
	endereco = models.CharField(max_length=350,null=False, blank=False, default='Endereço')
	dias = models.CharField(max_length=50, null=True, blank=True)
	horario = models.IntegerField(null=True, blank=True)
	foto = models.ImageField(upload_to="doacao_image/")

	def __str__(self):
		return self.local

	class Meta:
		verbose_name_plural = 'Pontos de arrecadação'
		verbose_name = 'Ponto de arrecadação'

#Model Eventos
class Eventos(models.Model):
	Nome = models.CharField(max_length=100, null=True, blank=True)
	Foto = models.ImageField(upload_to="evento_image/")
	Postagem = models.URLField(default="", blank=True)

	def __str__(self):
		return self.Nome

	class Meta:
		verbose_name_plural = 'Eventos'
		verbose_name = 'Evento'

