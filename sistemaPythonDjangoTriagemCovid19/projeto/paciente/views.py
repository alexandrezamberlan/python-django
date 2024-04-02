from __future__ import unicode_literals

from django.contrib import messages

from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin, EnfermeiroRequiredMixin

from .models import Paciente


class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
 

class PacienteCreateView(LoginRequiredMixin, EnfermeiroRequiredMixin, CreateView):
    model = Paciente
    fields = ['nome', 'sexo', 'data_nascimento', 'cpf', 'email', 'is_active']
    success_url = 'paciente_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Paciente cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)


class PacienteUpdateView(LoginRequiredMixin, EnfermeiroRequiredMixin, UpdateView):
    model = Paciente
    fields = ['nome', 'sexo', 'data_nascimento', 'cpf', 'email', 'is_active']
    success_url = 'paciente_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Paciente atualizado com sucesso na plataforma!')
        return reverse(self.success_url) 


class PacienteDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Paciente
    success_url = 'paciente_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à esse Paciente, permissão negada!')
        return redirect(self.success_url)