from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin

from .models import Unidade


class UnidadeListView(LoginRequiredMixin, ListView):
    model = Unidade
 

class UnidadeCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Unidade
    fields = ['nome', 'endereco', 'coordenador', 'fone', 'is_active']
    success_url = 'unidade_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Unidade cadastrada com sucesso na plataforma!')
        return reverse(self.success_url)


class UnidadeUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Unidade
    fields = ['nome','endereco', 'coordenador', 'fone', 'is_active']
    success_url = 'unidade_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Dados do Unidade atualizados com sucesso na plataforma!')
        return reverse(self.success_url) 


class UnidadeDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Unidade
    success_url = 'unidade_list'

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
            messages.error(request, 'Há dependências ligadas à essa Unidade, permissão negada!')
        return redirect(self.success_url)