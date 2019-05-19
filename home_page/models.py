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
        return self.conta_bancaria

    class Meta:
        verbose_name = 'Contas Bancária'

#Model Doacao
class Doacao(models.Model):
	voluntario = models.CharField(max_length=100, blank=False, null=False)
	local = models.TextField(null=False, blank=False)
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
	foto = models.ImageField(upload_to="evento_image/")
	local = models.TextField(null=False, blank=False)
	dia = models.CharField(max_length=50, null=True, blank=True)
	horario = models.IntegerField(null=True, blank=True)
	infoEvento = models.TextField(null=False, blank=False)
	infoAnimais = models.TextField(null=False, blank=False)

	def __str__(self):
		return self.local

	class Meta:
		verbose_name_plural = 'Eventos'
		verbose_name = 'Evento'

#Model Eventos


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

