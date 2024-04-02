from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from utils.decorators import LoginRequiredMixin,  StaffRequiredMixin

from .models import Consulta
from .forms import ConsultaForm


class ConsultaListView(LoginRequiredMixin,  ListView):
    model = Consulta
    
class ConsultaCreateView(LoginRequiredMixin, CreateView):
    model = Consulta
    # fields = ['medico','unidade', 'paciente', 'prescricao', 'medicamentos']
    form_class = ConsultaForm
    success_url = 'consulta_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Consulta regustrada com sucesso na plataforma!')
        return reverse(self.success_url)


class ConsultaUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Consulta
    # fields = ['medico','unidade', 'paciente', 'prescricao', 'medicamentos']
    form_class = ConsultaForm
    success_url = 'consulta_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Dados da Consulta atualizados com sucesso na plataforma!')
        return reverse(self.success_url)


class ConsultaDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Consulta
    success_url = 'consulta_list'

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
            messages.error(request, 'Há dependências ligadas a essa Consulta, permissão negada!')
        return redirect(self.success_url)