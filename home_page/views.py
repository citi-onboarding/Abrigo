from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from templated_email import send_templated_mail
from .models import *

# Create your views here.

class HomeView(generic.TemplateView):
	template_name = 'base.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["eventos"] = Eventos.objects.all()
		context["doacao"] = Doacao.objects.all()
		context["contas"] = Contas.objects.all()
		return context

	def post(self, request, *args, **kwargs):
			nome = request.POST.get('nome-contato')
			telefone = request.POST.get('telefone-contato')
			email = request.POST.get('email-contato')
			assunto = request.POST.get('assunto-contato')
			mensagem = request.POST.get('mensagem-contato')
			send_templated_mail(
				template_name='contact',
				from_email = email,
				recipient_list=['noreply.abrigodoseualberto@gmail.com'],
				context={
					'nome': nome,
					'telefone': telefone,
					'email': email,
					'assunto': assunto,
					'mensagem': mensagem,
				},
			)
			return HttpResponseRedirect(reverse_lazy("home_page:Home-Page"))

