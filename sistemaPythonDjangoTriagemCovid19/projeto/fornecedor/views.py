from __future__ import unicode_literals

from django.contrib import messages

from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from utils.decorators import LoginRequiredMixin, StaffRequiredMixin, EnfermeiroRequiredMixin

from .models import Fornecedor


class FornecedorListView(LoginRequiredMixin, ListView):
    model = Fornecedor
 

class FornecedorCreateView(LoginRequiredMixin, EnfermeiroRequiredMixin, CreateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'cidade', 'tipo_fornecedor', 'is_active']
    success_url = 'fornecedor_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Fornecedor cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)


class FornecedorUpdateView(LoginRequiredMixin, EnfermeiroRequiredMixin, UpdateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'cidade', 'tipo_fornecedor', 'is_active']
    success_url = 'fornecedor_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Fornecedor atualizado com sucesso na plataforma!')
        return reverse(self.success_url) 


class FornecedorDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Fornecedor
    success_url = 'fornecedor_list'

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
            messages.error(request, 'Há dependências ligadas à esse Fornecedor, permissão negada!')
        return redirect(self.success_url)