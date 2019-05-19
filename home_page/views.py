from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from templated_email import send_templated_mail

# Create your views here.

def home(request):
    return render(request, 'home_page/home.html')

class ContatoView(generic.TemplateView):
    template_name = 
