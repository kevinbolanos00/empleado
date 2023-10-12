from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
# Create your views here.
from .models import Prueba
from django.urls import reverse_lazy, reverse
from .forms import PruebaForm

#agg
from django.contrib.auth.mixins import LoginRequiredMixin


#agg
#@login_required
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'home/inicio.html'
    login_url = reverse_lazy('users_app:user-login')


class ResumenFoundationView(TemplateView):
    template_name = "home/resume_foundation.html"
    

class PruebaListView(ListView):
        template_name = 'home/lista.html'
        queryset = ['A','B','C']
        context_object_name = 'lista_prueba'


class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name='lista_prueba'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class= PruebaForm
    #fields=['titulo','subtitulo','catidad']
    success_url='/'
    
        