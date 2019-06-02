from django.db import models

# Create your models here.

#Model Bancos

class Contas(models.Model):
    foto = models.ImageField(upload_to='contas_image/')
    conta_bancaria = models.IntegerField(blank=False, null=True)
    numero_agencia = models.IntegerField(blank=False, null=True)
    nome_titular = models.CharField(max_length=100, blank=False, null=True)
    codigo_banco = models.IntegerField(blank=False, null=True)
    cpf = models.IntegerField(blank=False, null=True)
    def __str__(self):
        return self.nome_titular

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

#Model Picpay

class Picpay(models.Model):
	usuario = models.CharField(max_length=50, blank=False, null=True)

	def __str__(self):
		return  self.usuario

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'

#Model Apoia-se

class Apoia(models.Model):
	link = models.CharField(max_length=400,blank=False, null=True)    

	def __str__(self):
		return self.link

	class Meta:
		verbose_name_plural = 'Apoia-se'
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

