
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from aplications import departamento
from aplications.persona.models import Empleado
from django.urls import reverse_lazy
from .models import Departamento

from .forms import NewDepartamentoForm

#from aplications import departamento
#from .models import Departamento



class DepartamentoListView(LoginRequiredMixin, ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name='departamentos'
    login_url = reverse_lazy('users_app:user-login')



class NewDepartamentoView(LoginRequiredMixin, FormView):
    template_name='departamento/new_departamento.html'
    
    form_class= NewDepartamentoForm
    login_url = reverse_lazy('users_app:user-login')
    success_url='/'

    def form_valid(self, form):
        depa= Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname']
            
        )
        depa.save()
        nombre=form.cleaned_data['nombre']
        apellido=form.cleaned_data['apellidos']

        Empleado.objects.create(
           first_name=nombre,
           last_name=apellido,
           job='1',
           departamento=depa
        )


        
        return super(NewDepartamentoView, self).form_valid(form)

        
